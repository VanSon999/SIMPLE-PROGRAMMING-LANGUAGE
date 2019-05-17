
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    ################
    def __str__(self):
        return "MType([" + ','.join(str(x) for x in self.partype) + '],' + str(self.rettype) +')'
    ################
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    ################
    def __str__(self):
        return "Symbol(" + self.name + ',' + str(self.mtype) + ')'
    ################
class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([],VoidType()))]
    
    fun_check = None
    def __init__(self,ast):
        self.ast = ast
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def toSymbol(self,ast):
        if type(ast) == VarDecl:
            return Symbol(ast.variable.name,ast.varType)
        else: 
            return Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))

    def check_param_1(patype,param,ast,kind): #kind = True: procedure va nguoc lai
        if len(patype) != len(param):
            raise TypeMismatchInStatement(ast) if kind == True else TypeMismatchInExpression(ast)
        elif False in [StaticChecker.check_param_2(x,y) for x,y in zip(patype,[x[1] for x in param])]:
            raise TypeMismatchInStatement(ast) if kind == True else TypeMismatchInExpression(ast)
        return None
    
    def check_param_2(a,b):
        if type(a) is ArrayType and type(b) is ArrayType:
            return a.lower == b.lower and a.upper == b.upper and (type(a.eleType) == type(b.eleType))
        return type(a) == type(b) or (type(a) is FloatType and type(b) is IntType)

    def checkUndeclared(self,name_,env,kind):
        sym = self.lookup(name_.lower(),env,lambda x: x.name.lower()) # la bien hoac ham duoc su dung den
        if sym is None:
            if kind == "Identifier":
                kind_ = Identifier()
            elif kind == "Function":
                kind_ = Function()
            else:
                kind_ = Procedure()
            raise Undeclared(kind_,name_)
    
        elif (type(sym.mtype) != MType or type(sym.mtype.rettype) == VoidType) and (kind == "Function"):
            # print(sym)
            raise Undeclared(Function(),name_)
        elif (type(sym.mtype) != MType or type(sym.mtype.rettype) != VoidType) and (kind == "Procedure"):
            raise Undeclared(Procedure(),name_)
        elif (type(sym.mtype) == MType) and (kind == "Identifier"):
            raise Undeclared(Identifier(),name_)
        else:
            return (sym.name,sym.mtype)

    def checkRedeclared(self,sym,env,kind):
        if self.lookup(sym.name.lower(),env,lambda x: x.name.lower()):
            raise Redeclared(kind,sym.name)
        else:
            return sym

    def checkTypeMismatchInExpression():

        pass

    def checkTypeMismatchInStatement(stmt):
        raise TypeMismatchInStatement(stmt)

    def checkFunctionNotReturn():
        pass

    def checkBreakNotInLoop():
        pass

    def checkContinueNotInLoop():
        pass

    def checkNoEntryPoint(self,env):

        check = self.lookup("main",env,lambda x: x.name.lower())
        # print(check)
        if check is None:
            raise NoEntryPoint()
        elif type(check.mtype) != MType:
            raise NoEntryPoint()
        elif check.mtype.partype != []:
            raise NoEntryPoint()
        elif type(check.mtype.rettype) != VoidType:
            raise NoEntryPoint()
        else:
            return None

    def checkUnreachableStatement():
        pass

    def checkUnreachable():
        pass
        
##############################################################
    def visitProgram(self, ast, c): # da xu li duoc checkRedeclared va NoEntryPoint
        # prog = reduce(lambda x,y: [self.visit(y,x+c)] + x, ast.decl,[])
        prog = reduce(lambda x,y: [self.toSymbol(y)] + x, ast.decl,[]) + c #danh sach bien toan cuc
        # print(',  '.join(str(x) for x in prog))
        # self.checkNoEntryPoint(prog)
        
        # print('[' + ','.join(str(x) for x in prog) + ']\n')
        (reduce(lambda x,y: [self.visit(y,(x+c,prog))] + x, ast.decl,[])) 
        self.checkNoEntryPoint(prog)
        return None
     
    def visitVarDecl(self, ast, c): #chi moi co checkRedeclared
        # print(c[0])
        # print(ast)
        if type(c) == tuple:
            return (self.checkRedeclared(Symbol(ast.variable.name,ast.varType),c[0],Variable()))
        else:
            return (self.checkRedeclared(Symbol(ast.variable.name,ast.varType),c,Variable()))
    
    def visitFuncDecl(self, ast, c): #chi moi co checkRedeclared
        # print(ast)
        StaticChecker.fun_check = Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType)) #test fun/procedure dang visit toi
        #########
        lenpara = len(ast.param)
        symlist = []
        for x in ast.param + ast.local:
            syx = self.visit(x,[])
            if lenpara > 0:
                self.checkRedeclared(syx,symlist,Parameter())
            else:
                self.checkRedeclared(syx,symlist,Variable())  

            symlist = [syx] + symlist
            lenpara = lenpara - 1

        #######################################
        body = [self.visit(x,symlist + c[1]) for x in ast.body] 
        #######################################
        if True in list(map(lambda x: x[1],body)):
            raise BreakNotInLoop()
        if True in list(map(lambda x: x[2],body)):
            raise ContinueNotInLoop()
        if type(StaticChecker.fun_check.mtype.rettype) is not VoidType:
            #If it is a function -> there must be a return
            if True not in list(map(lambda x: x[0],body)):
                raise FunctionNotReturn(ast.name.name)

        kind_func = Procedure() if type(ast.returnType) == VoidType else Function()
        return (self.checkRedeclared(Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType)),c[0],kind_func))
    
    def visitIntType(self, ast, c):
        return IntType()
    
    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitArrayType(self, ast, c):
        return ArrayType(ast.lower,ast.upper,ast.eleType)
    
    def visitBinaryOp(self, ast, c):  # chi moi checkUndeclared
        left_ = self.visit(ast.left,c)
        right_ = self.visit(ast.right,c)

        if (type(left_[1]) == StringType) or (type(right_[1]) == StringType):
            raise TypeMismatchInExpression(ast)
        
        if (type(left_[1]) == IntType) and (type(right_[1]) == IntType): 
            if ast.op in ['+','-','*','div','mod']:
                return ("integer",IntType())
            if ast.op in ['=','<>','<','<=','>','>=']: 
                return ("boolean",BoolType())
            if ast.op == '/':
                return ("real",FloatType())
        
        if type(left_[1]) is FloatType or type(right_[1]) is FloatType: #second case
            if ast.op in ['+','-','*','/']:
                return ("real",FloatType())
            if ast.op in ['=','<>','<','<=','>','>=']:
                return ("boolean",BoolType())
        
        if type(left_[1]) is BoolType and type(right_[1]) is BoolType: #third case
            if ast.op in ['and','andthen','or','orelse']:
                return ("boolean",BoolType())
                
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast, c): 
        body_ = self.visit(ast.body,c)

        if ast.op == '-' and type(body_[1]) is IntType:
            return ("integer",IntType())
        if ast.op == '-' and type(body_[1]) is FloatType:
            return ("real",FloatType())
        if ast.op == 'not' and type(body_[1]) is BoolType:
            return ("boolean",BoolType())

        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, c): 
        # print(ast)
        method_ = self.visit(ast.method,(c,"Function"))

        param_ = [self.visit(x,c) for x in ast.param]

        StaticChecker.check_param_1(method_[1].partype ,param_,ast,False) # function tuong duong voi false
        # print(ast)
        return (ast.method.name,method_[1].rettype)
    
    def visitId(self, ast, c): # chi moi checkUndeclared
        if type(c) == tuple:
            # print(ast)
            # print('   ,   ' .join(str(x) for x in c[0]))
            return self.checkUndeclared(ast.name,c[0],c[1])
        else:
            return self.checkUndeclared(ast.name,c,"Identifier")
    
    def visitArrayCell(self, ast, c): 
        arr_ = self.visit(ast.arr,c)

        idx_ = self.visit(ast.idx,c)

        if (type(arr_[1]) != ArrayType) or (type(idx_[1]) != IntType):
            raise TypeMismatchInExpression(ast)
        
        return (arr_[0],arr_[1].eleType)
    
    def visitAssign(self, ast, c): 
        # ve trai
        # print(ast)
        lhs_ = self.visit(ast.lhs,c)
        # print(ast.lhs)
        # print(lhs_[0],lhs_[1])
        if (type(lhs_[1]) in [StringType,ArrayType]):
            raise TypeMismatchInStatement(ast)

        #ve phai
        exp_ = self.visit(ast.exp,c)
        if not ((type(lhs_[1]) == FloatType and type(exp_[1]) == IntType) or type(lhs_[1]) == type(exp_[1])):
            raise TypeMismatchInStatement(ast)

        return (False,False,False)

    def visitWith(self, ast, c): # chi moi checkUndeclared
        decl_with = reduce(lambda x,y: [self.visit(y,x)] + x, ast.decl, [])
        body_with = [self.visit(x,decl_with + c) for x in ast.stmt]
        return reduce(lambda x,y: (x[0] or y[0],x[1] or y[1],x[2] or y[2]),body_with) if len(body_with) != 0 else (False,False,False)
    
    def visitIf(self, ast, c): # chi moi checkUndeclared
        test_ = False #kiem tra trong vong lap
        if type(c) == tuple:
            c_ = c[0]
            test_ = c[1]
        else:
            c_ = c

        expr_ = self.visit(ast.expr,c_)
        if type(expr_[1]) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        thenstmt_ = [self.visit(x,c_) for x in ast.thenStmt]
        res_1 = reduce(lambda x,y: (x[0] or y[0], x[1] or y[1], x[2] or y[2]),thenstmt_) if len(thenstmt_) != 0 else (False,False,False)

        elsestmt_ = [self.visit(x,c_) for x in ast.elseStmt]
        res_2 = reduce(lambda x,y: (x[0] or y[0], x[1] or y[1], x[2] or y[2]),elsestmt_) if len(elsestmt_) != 0 else (False,False,False)

        if test_:    #trong vong lap 
            res_3 = (reduce(lambda x,y: x or y, res_1)) and (reduce(lambda x,y: x or y, res_2)) #can xem lai~!!!!
            return (res_3,res_3,res_3)
        else:
            return (res_1[0] and res_2[0], res_1[1] or res_2[1], res_1[2] or res_2[2])
    
    def visitFor(self, ast, c): # chi moi checkUndeclared
        id_ = self.visit(ast.id,c)
        if type(id_[1]) != IntType:
            raise TypeMismatchInStatement(ast)

        expr1_ = self.visit(ast.expr1,c)
        if type(expr1_[1]) != IntType:
            raise TypeMismatchInStatement(ast)

        expr2_ = self.visit(ast.expr2,c)
        if type(expr2_[1]) != IntType:
            raise TypeMismatchInStatement(ast)

        # (self.visit(ast.up,c)) #co the khong can thiet
        
        loop_ = [self.visit(x,(c,True)) if type(x) == If else self.visit(x,c) for x in ast.loop]
        return (False,False,False) #return, break, continue
    
    def visitContinue(self, ast, c):
        return (False,False,True) # return , break, continue
        # return None
    
    def visitBreak(self, ast, c):
        return (False,True,False)
        # return None
    
    def visitReturn(self, ast, c): 
        if ast.expr is not None:
            expr_ = self.visit(ast.expr,c)
            if type(StaticChecker.fun_check.mtype.rettype) == VoidType: #procedure
                raise TypeMismatchInStatement(ast)
            else:
                if expr_[1] is None:
                    raise TypeMismatchInStatement(ast)
                temp = StaticChecker.fun_check.mtype.rettype
                if (type(expr_[1]) == ArrayType):
                    if ((type(expr_[1]) != type(temp)) or (expr_[1].lower != temp.lower) or (expr_[1].upper != temp.upper) or (type(expr_[1].eleType) != type(temp.eleType))):
                        # print(ast)
                        raise TypeMismatchInStatement(ast)
                if type(expr_[1]) != type(temp) and not (type(expr_[1]) == IntType and type(temp) == FloatType):
                    # print(ast)
                    raise TypeMismatchInStatement(ast)
        else:
            if type(StaticChecker.fun_check.mtype.rettype) != VoidType: #function
                raise TypeMismatchInStatement(ast)

        return (True,False,False)
    
    def visitWhile(self, ast, c): 
        exp_ = self.visit(ast.exp,c)
        if type(exp_[1]) != BoolType:
            raise TypeMismatchInStatement(ast)

        sl_ = [self.visit(x,(c,True)) if type(x) == If else self.visit(x,c) for x in ast.sl]

        return (False,False,False)
    
    def visitCallStmt(self, ast, c): # Note!!!!!!!!!!
        # print(ast)
        method_ = self.visit(ast.method,(c,"Procedure"))

        param_ = [self.visit(x,c) for x in ast.param]
        #check param co trung khop voi khai bao!
        StaticChecker.check_param_1(method_[1].partype ,param_,ast,True)
        return (False,False,False)
    
    def visitIntLiteral(self, ast, c):
        return ("integer",IntType())
    
    def visitFloatLiteral(self, ast, c):
        return ("real",FloatType())
    
    def visitBooleanLiteral(self, ast, c):
        return ("boolean",BoolType())
    
    def visitStringLiteral(self, ast, c):
        return ("string",StringType())

#########################################################---END---###########################################################
# def visitProgram(self,ast, c): 
    #     return [self.visit(x,c) for x in ast.decl]

    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body)) 
    

    # def visitCallStmt(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
    #         raise Undeclared(Procedure(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         raise TypeMismatchInStatement(ast)            
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()