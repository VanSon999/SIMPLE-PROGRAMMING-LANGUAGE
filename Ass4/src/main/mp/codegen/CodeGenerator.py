'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(Frame(None,None), self.env)
        list_fun = []
        #visit de tao sym
        for x in ast.decl:
            if type(x) is FuncDecl:
                list_fun = list_fun + [x]
            else:
                e = self.visit(x, e)
        # print(','.join(str(x) for x in e.sym))
        # visit doi voi fun_decl de tao constructor
        # print(','.join(str(x) for x in list_fun))
        for x in list_fun:
            e = self.visit(x,e)

        # print(','.join(str(x) for x in e.sym))
        en_sym = e.sym
        for func in list_fun:
            # print(func)
            e.frame.name = func.name
            e.frame.returnType = func.returnType
            self.genMETHOD(func,en_sym,e.frame)

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), e.sym, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: sym
        #frame: Frame
        # print(','.join(str(x) for x in o))
        isInit = consdecl.name.name.lower() == "<init>" #or (consdecl.returnType is None)
        
        isMain = consdecl.name.name.lower() == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        # print(isMain)
        returnType = VoidType() if isInit else consdecl.returnType
        
        methodName = "<init>" if isInit else consdecl.name.name

        intype = None
        if isInit: #constructor
            intype = list()

        elif isMain: #main
            intype = [ArrayPointerType(StringType())] #Note.........................................

        else: #function and proceduce
            intype = [x.varType for x in consdecl.param]
            # print(','.join(str(x) for x in intype))

        mtype = MType(intype, returnType)

        if isMain or isInit:
            self.emit.printout(self.emit.emitMETHOD(methodName.lower(), mtype, not isInit, frame))
        else:
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)

        glenv = o # sym

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        if isMain:
            # self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(None,None,StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)) # Note..............................................

        e = SubBody(frame,glenv)
        body = consdecl.body

        if not isInit:
            for x in consdecl.param:
                e = self.visit(x,e)
            
            for y in consdecl.local:
                e = self.visit(y,e)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        #Note...............................................
        #phan xu li array cho ki su tai nang bo qua!!!!
        #Note...............................................
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        list(map(lambda x: self.visit(x, SubBody(frame, e.sym)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

#####################################################Decl#################################################################

    def visitVarDecl(self, ast, o):
        subctxt = o
        frame_ = o.frame
        sym_ = o.sym

        check_local = (len(frame_.indexLocal) != 0)

        if check_local: #bien local
            idex = frame_.getNewIndex()
            var_dec1 = self.emit.emitVAR(idex,ast.variable.name,ast.varType,frame_.getStartLabel(),frame_.getEndLabel(),frame_)
            sym_ = sym_ + [Symbol(ast.variable.name,ast.varType,idex)]
            self.emit.printout(var_dec1)

        else: #bien global
            var_dec2 = self.emit.emitATTRIBUTE(ast.variable.name,ast.varType,False,None)
            sym_ = sym_ + [Symbol(ast.variable.name,ast.varType,None)]
            self.emit.printout(var_dec2)
        
        return SubBody(frame_,sym_)

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        sym_ = o.sym
        frame_ = o.frame

        if frame_ is None:
            frame_ = Frame(ast.name,ast.returnType)

        else:
            frame_.name = ast.name
            frame_.returnType = ast.returnType

        return SubBody(frame_, sym_ + [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))])

#############################################Statement################################################

    def visitAssign(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame
        # print(ast)
        #visit left : 1 la code , 2 la type
        # left_1 ,left_2 = self.visit(ast.lhs, Access(frame_,sym_,True,True)) danh cho arraycell ma array khong dung den 
        #Note...........................
        #visit right:

        right_1, right_2 = self.visit(ast.exp,Access(frame_,sym_,False,False))
        #visit left:

        left_1,left_2 = self.visit(ast.lhs, Access(frame_,sym_,True,False))

        #ep kieu
        if (type(left_2) is FloatType) and (type(right_2) is IntType): #note..................................
            right_1 = right_1 + self.emit.emitI2F(frame_)

        self.emit.printout(right_1 + left_1)

    def visitIf(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame

        #exp_1 la code , exp_2 la kieu
        exp_1,exp_2 = self.visit(ast.expr,Access(frame_ ,sym_ ,False,False))
        self.emit.printout(exp_1)

        thenLabel = frame_.getNewLabel()
        elseLabel = frame_.getNewLabel()

        self.emit.printout(self.emit.emitIFTRUE(thenLabel,frame_))

        if ast.elseStmt != []:
            e_2 = SubBody(frame_,sym_)
            list(map(lambda x: self.visit(x, e_2), ast.elseStmt))

        self.emit.printout(self.emit.emitGOTO(elseLabel,frame_))
        self.emit.printout(self.emit.emitLABEL(thenLabel,frame_))

        e_1 = SubBody(frame_,sym_)
        list(map(lambda x: self.visit(x, e_1), ast.thenStmt))
        self.emit.printout(self.emit.emitLABEL(elseLabel,frame_))

    # def visitFor(self, ast, o):
    #     subctxt = o
    #     sym_ = subctxt.sym
    #     frame_ = subctxt.frame
    #     var = self.lookup(ast.id.name.lower(),sym_[::-1],lambda x: x.name.lower())
    #     # print(var)
    #     # print(";".join(str(x) for x in sym_))
    #     expr_ = None
    #     if ast.up == True:
    #         expr_ = Assign(ast.id,BinaryOp('-' ,ast.expr1 ,IntLiteral(1)))
    #     else:
    #         expr_ = Assign(ast.id,BinaryOp('+' ,ast.expr1 ,IntLiteral(1)))

    #     # print(expr_)
    #     esub = SubBody(frame_,sym_)
    #     self.visit(expr_, esub)
    #     # print(temp[0])
    #     esub.frame.enterLoop()
    #     continue_ = esub.frame.getContinueLabel()
    #     break_ = esub.frame.getBreakLabel()
    #     self.emit.printout(self.emit.emitLABEL(continue_,esub.frame))

    #     if var.value is not None:
    #         self.emit.printout(self.emit.emitREADVAR(var.name ,var.mtype ,var.value ,esub.frame))
    #     else:
    #         self.emit.printout(self.emit.emitGETSTATIC("io" + "." + var.name, var.mtype ,esub.frame))
    #     self.emit.printout(self.emit.emitPUSHICONST(1 ,esub.frame))

    #     if ast.up == True: #up
    #         self.emit.printout(self.emit.emitADDOP('+' ,IntType() ,esub.frame))
    #     else:
    #         self.emit.printout(self.emit.emitADDOP('-' ,IntType() ,esub.frame))

    #     if var.value is not None:
    #         self.emit.printout(self.emit.emitWRITEVAR(var.name ,var.mtype ,var.value ,esub.frame))
    #     else:
    #         self.emit.printout(self.emit.emitPUTSTATIC("io" + "." + var.name ,var.mtype , esub.frame))

    #     if var.value is not None:
    #         self.emit.printout(self.emit.emitREADVAR(var.name ,var.mtype ,var.value , esub.frame))
    #     else:
    #         self.emit.printout(self.emit.emitGETSTATIC("io" + "." + var.name ,var.mtype, esub.frame))

    #     exp_2,texp_2 = self.visit(ast.expr2,Access(esub.frame , esub.sym ,False,False))
    #     self.emit.printout(exp_2)

    #     if ast.up == True: #up
    #         self.emit.printout(self.emit.emitREOP('<=',IntType(), esub.frame))
    #     else:
    #         self.emit.printout(self.emit.emitREOP('>=',IntType(), esub.frame))
    #     self.emit.printout(self.emit.emitIFFALSE(break_, esub.frame))

    #     e = SubBody(esub.frame, esub.sym)
    #     list(map(lambda x: self.visit(x, e), ast.loop))

    #     self.emit.printout(self.emit.emitGOTO(continue_ ,esub.frame))
    #     self.emit.printout(self.emit.emitLABEL(break_ ,esub.frame))
        
    #     esub.frame.exitLoop()

    def visitFor(self, ast, o):
 
        subctxt = o
        frame_ = subctxt.frame
        sym_ = subctxt.sym
 
        labelfor = frame_.getNewLabel()
 
        frame_.enterLoop()
        accessT = Access(frame_, sym_, True, False)
        accessF = Access(frame_, sym_, False, False)
       
        expr1_, texpr1_ = self.visit(ast.expr1, Access(frame_, sym_, False, False))
        
        id_, tid_ = self.visit(ast.id, Access(frame_, sym_, True, False))
        
        self.emit.printout(expr1_)
        self.emit.printout(id_)
        
        self.emit.printout(self.emit.emitLABEL(labelfor, frame_))
 
        continue_ = frame_.getContinueLabel()
        break_ = frame_.getBreakLabel()
 
        if ast.up is True:
            id_, tid_ = self.visit(ast.id, Access(frame_, sym_, False, False))
            self.emit.printout(id_)
            expr2_, texpr2_ = self.visit(ast.expr2, Access(frame_, sym_, False, False))
            self.emit.printout(expr2_)
            self.emit.printout(self.emit.emitIFICMPGT(break_, frame_))

        else:
            id_, tid_ = self.visit(ast.id, Access(frame_, sym_, False, False))
            self.emit.printout(id_)
            expr2_, texpr2_ = self.visit(ast.expr2, Access(frame_, sym_, False, False))
            self.emit.printout(expr2_)
            self.emit.printout(self.emit.emitIFICMPLT(break_, frame_))
 
        list(map(lambda x: self.visit(x, o), ast.loop))
        self.emit.printout(self.emit.emitLABEL(continue_, frame_))
 
        if ast.up is True:
            expr_, texpr_ = self.visit(BinaryOp('+', ast.id, IntLiteral(1)), Access(frame_, sym_, False, False))
            id__, tid__ = self.visit(ast.id, Access(frame_, sym_, True, False))
            self.emit.printout(expr_)
            self.emit.printout(id__)

        else:
            expr_, texpr_= self.visit(BinaryOp('-', ast.id, IntLiteral(1)), Access(frame_, sym_, False, False))
            id__, tid__ = self.visit(ast.id, Access(frame_, sym_, True, False))
            self.emit.printout(expr_)
            self.emit.printout(id__)

        self.emit.printout(self.emit.emitGOTO(labelfor, frame_))
        self.emit.printout(self.emit.emitLABEL(break_, frame_))

        frame_.exitLoop()

    def visitWhile(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame

        frame_.enterLoop()
        continue_ = frame_.getContinueLabel()
        break_ = frame_.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(continue_ ,frame_))

        exp_ , texp_ = self.visit(ast.exp,Access(frame_ ,sym_ ,False ,False))
        self.emit.printout(exp_)
        self.emit.printout(self.emit.emitIFFALSE(break_ ,frame_))

        e_ = SubBody(frame_ , sym_)
        list(map(lambda x: self.visit(x, e_), ast.sl))

        self.emit.printout(self.emit.emitGOTO(continue_ ,frame_))
        self.emit.printout(self.emit.emitLABEL(break_ ,frame_))

        frame_.exitLoop()

    def visitBreak(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame

        break_ = frame_.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(break_, frame_))
    
    def visitContinue(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame

        continue_ = frame_.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continue_, frame_))

    def visitReturn(self, ast, o):
        subctxt = o
        sym_ = subctxt.sym
        frame_ = subctxt.frame

        if ast.expr is not None:
            exp_ , texp_ = self.visit(ast.expr ,Access(frame_ ,sym_ ,False,False))
            self.emit.printout(exp_)

            if (type(texp_) is IntType) and (type(frame_.returnType) is FloatType):
                self.emit.printout(self.emit.emitI2F(frame_))

        self.emit.printout(self.emit.emitGOTO(frame_.getEndLabel() , frame_ ))

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # print(ast)
        #tim ham tuong ung de goi
        sym = self.lookup(ast.method.name.lower(), nenv[::-1], lambda x: x.name.lower())
        # print(sym)
        # print(sym)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", [])
        idx_ = 0
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, False))
            in_ = (in_[0] + str1, in_[1] + [typ1])

            if (type(sym.mtype.partype[idx_]) is FloatType) and (type(typ1) is IntType):
                in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])

            idx_ = idx_ + 1
        # print(str1,typ1)
        # print(in_[0])
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))

    def visitWith(self, ast, o):
        ctxt = o
        frame_ = ctxt.frame
        sym_ = [];[sym_.append(x) for x in ctxt.sym]

        frame_.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame_.getStartLabel(), frame_))

        e = SubBody(frame_, sym_)

        for x in ast.decl:
            e = self.visit(x, e)

        list(map(lambda x: self.visit(x, e), ast.stmt))
        #xoa bien cuc bo trong With
        e.sym = e.sym[:len(e.sym) - len(ast.decl)]

        self.emit.printout(self.emit.emitLABEL(frame_.getEndLabel(), frame_))
        frame_.exitScope()

##########################################Exp#############################################
    def visitArrayCell(self, ast, o):#bo qua vi khong lam phan array!!!
        pass 

    def visitId(self, ast, o):
        subctxt = o 
        frame_ = subctxt.frame
        sym_ = subctxt.sym
        # print(','.join(str(x) for x in sym_))
        # print(ast)
        isLeft_ = subctxt.isLeft
        isFirst_ = subctxt.isFirst
        sym_id = self.lookup(ast.name.lower(),sym_[::-1],lambda x: x.name.lower())
        # print(sym_id)
        #khong lam kieu array nen khong quan tam isFirst
        if not isLeft_ and not isFirst_: #danh cho ve phai
            # print(1)
            if sym_id.value is None:
                return self.emit.emitGETSTATIC(self.className + "." + sym_id.name, sym_id.mtype, frame_), sym_id.mtype
            else:
                return self.emit.emitREADVAR(sym_id.name, sym_id.mtype, sym_id.value, frame_), sym_id.mtype

        if isLeft_ and not isFirst_: #danh cho ve trai
            # print(2)
            if type(sym_id.mtype) is not ArrayType:
                if sym_id.value is None:
                    return self.emit.emitPUTSTATIC(self.className + "." + sym_id.name , sym_id.mtype , frame_), sym_id.mtype
                else:
                    return self.emit.emitWRITEVAR(sym_id.name , sym_id.mtype , sym_id.value , frame_), sym_id.mtype
            # else:
            #     return self.emit.emitASTORE(id_info.mtype.eleType,frame),id_info.mtype.eleType # load array khong dung den

    def visitCallExpr(self, ast, o):
        subctxt = o
        frame_ = subctxt.frame
        sym_ = subctxt.sym
        isLeft = subctxt.isLeft
        isFirst = subctxt.isFirst
        
        sym_id = self.lookup(ast.method.name.lower(), sym_[::-1], lambda x: x.name.lower())
        cname = sym_id.value.value
        ctype = sym_id.mtype
        # print(sym_id)
        in_ = ("", [])
        idx_ = 0
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame_ , sym_, False, False))
            in_ = (in_[0] + str1, in_[1] + [typ1])

            if (type(sym_id.mtype.partype[idx_]) is FloatType) and (type(typ1) is IntType):
                in_ = (in_[0] + self.emit.emitI2F(frame_), in_[1])

            idx_ = idx_ + 1
        # print(str1, typ1)
        # print(in_[0])
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym_id.name, ctype, frame_) ,sym_id.mtype.rettype

    def visitUnaryOp(self, ast, o):
        subctxt = o
        frame_ = subctxt.frame
        sym_ = subctxt.sym

        unexp_ ,tunexp_ = self.visit(ast.body, Access(frame_, sym_, False, False))

        if (type(tunexp_) is IntType) and (ast.op == '-'):
            return unexp_ + self.emit.emitNEGOP(IntType(), frame_), IntType()

        if (type(tunexp_) is FloatType) and (ast.op == '-'):
            return unexp_ + self.emit.emitNEGOP(FloatType(), frame_), FloatType()

        if ast.op.lower() == 'not':
            return unexp_ + self.emit.emitNOT(BoolType(), frame_), BoolType()

    def visitBinaryOp(self, ast, o):
        subctxt = o
        frame_ = subctxt.frame
        sym_ = subctxt.sym
        # print(ast)
        lexp_ , tlexp_ = self.visit(ast.left, Access(frame_ ,sym_ ,False, False))
        # print(lexp_, tlexp_)
        rexp_ , trexp_ = self.visit(ast.right, Access(frame_ ,sym_ ,False, False))
        # print(rexp_, trexp_)
        if (type(tlexp_) is BoolType) or (type(trexp_) is BoolType):
            if ast.op.lower() == 'and':
                return lexp_ + rexp_ + self.emit.emitANDOP(frame_) , BoolType()

            elif ast.op.lower() == 'or':
                return lexp_ + rexp_ + self.emit.emitOROP(frame_) , BoolType()

            elif ast.op.lower() == 'andthen':
                label1 = frame_.getNewLabel()
                label2 = frame_.getNewLabel()
                code_j = lexp_
                code_j += self.emit.emitPUSHICONST(1, frame_)
                code_j += self.emit.emitANDOP(frame_)
                code_j += self.emit.emitIFFALSE(label2 , frame_)
                code_j += rexp_
                code_j += self.emit.emitPUSHICONST(1 , frame_)
                code_j += self.emit.emitANDOP(frame_)
                code_j += self.emit.emitIFFALSE(label2, frame_)
                code_j += self.emit.emitPUSHICONST(1, frame_)
                code_j += self.emit.emitGOTO(label1, frame_)
                code_j += self.emit.emitLABEL(label2, frame_)
                code_j += self.emit.emitPUSHICONST(0, frame_)
                code_j += self.emit.emitLABEL(label1, frame_)

                return code_j, BoolType()

            elif ast.op.lower() == 'orelse':
                label1 = frame_.getNewLabel()
                label2 = frame_.getNewLabel()
                code_j = rexp_
                code_j += self.emit.emitPUSHICONST(0, frame_)
                code_j += self.emit.emitOROP(frame_)
                code_j += self.emit.emitIFTRUE(label1, frame_)
                code_j += rexp_
                code_j += self.emit.emitPUSHICONST(0, frame_)
                code_j += self.emit.emitOROP(frame_)
                code_j += self.emit.emitIFTRUE(label1, frame_)
                code_j += self.emit.emitPUSHICONST(0, frame_)
                code_j += self.emit.emitGOTO(str(label2), frame_)
                code_j += self.emit.emitLABEL(label1, frame_)
                code_j += self.emit.emitPUSHICONST(1, frame_)
                code_j += self.emit.emitLABEL(label2, frame_)
                return code_j, BoolType()

            elif ast.op in ['=','<>']:
                return lexp_ + rexp_ + self.emit.emitREOP(ast.op , BoolType(), frame_), BoolType()

        if (type(tlexp_) is IntType) and (type(trexp_) is IntType):
            # print(1)
            if ast.op in ['+','-']:
                return lexp_ + rexp_ + self.emit.emitADDOP(ast.op ,IntType(), frame_), IntType()

            elif ast.op == '*':
                return lexp_ + rexp_ + self.emit.emitMULOP(ast.op, IntType(), frame_), IntType()

            elif ast.op.lower() == 'div':
                return lexp_ + rexp_ + self.emit.emitDIV(frame_), IntType()

            elif ast.op.lower() == 'mod':
                # print(1)
                return lexp_ + rexp_ + self.emit.emitMOD(frame_), IntType()

            elif ast.op == '/':
                lexp_ = lexp_ + self.emit.emitI2F(frame_)
                rexp_ = rexp_ + self.emit.emitI2F(frame_)
                return lexp_ + rexp_ + self.emit.emitMULOP(ast.op, FloatType(), frame_), FloatType()

            elif ast.op in ['<','<=','>','>=','<>','=']:
                # print(1)
                return lexp_ + rexp_ + self.emit.emitREOP(ast.op, IntType(), frame_), BoolType()

        #either left or right is FLoat
        if type(tlexp_) is IntType:
            lexp_ = lexp_ + self.emit.emitI2F(frame_)

        if type(trexp_) is IntType:
            rexp_ = rexp_ + self.emit.emitI2F(frame_) 

        if ast.op in ['+','-']:
            return lexp_ + rexp_ + self.emit.emitADDOP(ast.op, FloatType(), frame_), FloatType()

        elif ast.op in ['*','/']:
            return lexp_ + rexp_ + self.emit.emitMULOP(ast.op, FloatType(), frame_), FloatType() 

        elif ast.op in ['<','<=','>','>=','<>','=']:
            return lexp_ + rexp_ + self.emit.emitFREOP(ast.op, FloatType(), frame_), FloatType()

    # def visitBinaryOp(self, ast, o):
    #     #o: any
    #     #ast.op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
    #     #ast.left:Expr
    #     #ast.right:Expr

    #     ctxt = o
    #     frame = ctxt.frame
    #     nenv = ctxt.sym

    #     leftOprandstr, typL = self.visit(ast.left, Access(frame, nenv, False, False))
    #     rightOperandstr, typR = self.visit(ast.right, Access(frame, nenv, False, False))

    #     if type(typL) == type(typR):
    #         if type(typL) is BoolType:
    #             if ast.op.lower() == 'and':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitANDOP(frame), BoolType()   
    #             elif ast.op.lower() == 'or':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitOROP(frame), BoolType()
    #             elif ast.op.lower() == 'andthen':
    #                 # right, typR1 = self.visit(BooleanLiteral(False), o)
    #                 # lst = leftOprandstr + right + self.emit.emitREOP('==', IntType(), frame)
    #                 lst = list()
    #                 label1 = frame.getNewLabel()
    #                 label2 = frame.getNewLabel()
    #                 lst.append(leftOprandstr)
    #                 lst.append(self.emit.emitIFFALSE(label1, frame))
    #                 lst.append(rightOperandstr)
    #                 lst.append(self.emit.emitIFFALSE(label1, frame))
    #                 lst.append(self.emit.emitPUSHICONST("true", frame))
    #                 lst.append(self.emit.emitGOTO(label2,frame))
    #                 lst.append(self.emit.emitLABEL(label1,frame))
    #                 lst.append(self.emit.emitPUSHICONST("false", frame))
    #                 lst.append(self.emit.emitLABEL(label2,frame))
    #                 frame.pop()
    #                 return ''.join(lst), BoolType()
    #             elif ast.op.lower() == 'orelse':
    #                 # right, typR1 = self.visit(BooleanLiteral(True), o)
    #                 # lst = leftOprandstr + right + self.emit.emitREOP('==', IntType(), frame)
    #                 lst = list()
    #                 label1 = frame.getNewLabel()
    #                 label2 = frame.getNewLabel()
    #                 lst.append(leftOprandstr)
    #                 lst.append(self.emit.emitIFTRUE(label1, frame))
    #                 lst.append(rightOperandstr)
    #                 lst.append(self.emit.emitIFTRUE(label1, frame))
    #                 lst.append(self.emit.emitPUSHICONST("false", frame))
    #                 lst.append(self.emit.emitGOTO(label2,frame))
    #                 lst.append(self.emit.emitLABEL(label1,frame))
    #                 lst.append(self.emit.emitPUSHICONST("true", frame))
    #                 lst.append(self.emit.emitLABEL(label2,frame))
    #                 frame.pop()
    #                 return ''.join(lst), BoolType()
    #         elif type(typL) is IntType:
    #             if ast.op in ['+', '-']:
    #                 return leftOprandstr + rightOperandstr + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
    #             elif ast.op == '*':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
    #             elif ast.op.lower() == 'div':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitDIV(frame), IntType()
    #             elif ast.op.lower() == 'mod':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMOD(frame), IntType()
    #             elif ast.op in ['<', '<=', '>', '>=']:
    #                 return leftOprandstr + rightOperandstr + self.emit.emitREOP(ast.op, IntType(), frame), BoolType()
    #             elif ast.op == '<>':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitREOP('!=', IntType(), frame), BoolType()
    #             elif ast.op == '=':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitREOP('==', IntType(), frame), BoolType()
    #             elif ast.op == '/':
    #                 leftOprandstr += self.emit.emitI2F(frame)
    #                 rightOperandstr += self.emit.emitI2F(frame)
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #         elif type(typL) is FloatType:
    #             if ast.op in ['+', '-']:
    #                 return leftOprandstr + rightOperandstr + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
    #             elif ast.op == '*':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #             elif ast.op == '/':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #             elif ast.op in ['<', '<=', '>', '>=']:
    #                 return self.emit.emitFREOP(ast.op, leftOprandstr, rightOperandstr, frame), BoolType()
    #             elif ast.op == '<>':
    #                 return self.emit.emitFREOP('!=', leftOprandstr, rightOperandstr, frame), BoolType()
    #             elif ast.op == '=':
    #                 return self.emit.emitFREOP('==', leftOprandstr, rightOperandstr, frame), BoolType()
    #     else:
    #         if ast.op in ['+', '-']:
    #             if type(typL) is FloatType and type(typR) is IntType:
    #                 return leftOprandstr + rightOperandstr + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
    #             elif type(typL) is IntType and type(typR) is FloatType:
    #                 return leftOprandstr + self.emit.emitI2F(frame) + rightOperandstr + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
    #         elif ast.op == '*':
    #             if type(typL) is FloatType and type(typR) is IntType:
    #                 return leftOprandstr + rightOperandstr + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #             elif type(typL) is IntType and type(typR) is FloatType:
    #                 return leftOprandstr + self.emit.emitI2F(frame) + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #         else:
    #             if type(typL) is IntType: 
    #                 leftOprandstr += self.emit.emitI2F(frame)
    #             if type(typR) is IntType: 
    #                 rightOperandstr += self.emit.emitI2F(frame)
    #             if ast.op == '/':
    #                 return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
    #             elif ast.op in ['<', '<=', '>', '>=']:
    #                 return self.emit.emitFREOP(ast.op, leftOprandstr, rightOperandstr, frame), BoolType()
    #             elif ast.op == '<>':
    #                 return self.emit.emitFREOP('!=', leftOprandstr, rightOperandstr, frame), BoolType()
    #             elif ast.op == '=':
    #                 return self.emit.emitFREOP('==', leftOprandstr, rightOperandstr, frame), BoolType()
    
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('"' + ast.value + '"' ,StringType(), frame), StringType() #Note......................................
