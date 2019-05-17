from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import *
class ASTGeneration(MPVisitor):

    # program : decl* EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        lstdecl = []
        for x in ctx.decl():
            decl_ = self.visit(x)
            if type(decl_) == type([]):
                lstdecl = lstdecl + decl_
            else:
                lstdecl.append(decl_)
        return Program(lstdecl)

    # decl: var_decl_total | func_decl_total | proc_decl_total;
    def visitDecl(self,ctx:MPParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # var_decl_total: VAR var_decl+;
    def visitVar_decl_total(self,ctx:MPParser.Var_decl_totalContext):
        lstvar_decl = []
        for x in ctx.var_decl():
            lstvar_decl += self.visit(x)

        return lstvar_decl

    # var_decl: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array) SEMI;
    def visitVar_decl(self,ctx:MPParser.Var_declContext):
        if ctx.type_data() != None:
            type_ =  self.visit(ctx.type_data())
        else:
            type_ = self.visit(ctx.type_array())

        return [VarDecl(Id(x.getText()),type_) for x in ctx.IDENTIFIER()]

    # type_data: INTEGER | REAL | BOOLEAN | STRING; //////// can kiem tra lai
    def visitType_data(self,ctx:MPParser.Type_dataContext):
        if ctx.INTEGER() != None:
            return IntType()
        elif ctx.REAL() != None:
            return FloatType()
        elif ctx.BOOLEAN() != None:
            return BoolType()
        else:
            return StringType()
    
    # type_array: ARRAY LSB sub1? INTEGER_TYPE D_DOT sub2? INTEGER_TYPE RSB OF type_data;
    # def visitType_array(self,ctx:MPParser.Type_arrayContext):
    #     int1 = int('-' + ctx.INTEGER_TYPE(0).getText()) if ctx.sub1() != None else int(ctx.INTEGER_TYPE(0).getText())
    #     int2 = int('-' + ctx.INTEGER_TYPE(1).getText()) if ctx.sub2() != None else int(ctx.INTEGER_TYPE(1).getText())
    #     return ArrayType(int1,int2,self.visit(ctx.type_data()))
    # type_array: ARRAY LSB range_arr D_DOT range_arr RSB OF type_data;
    def visitType_array(self,ctx:MPParser.Type_arrayContext):
        int1 = self.visit(ctx.range_arr(0))
        int2 = self.visit(ctx.range_arr(1))
        return ArrayType(int1,int2,self.visit(ctx.type_data()))

    # range_arr: SUB? INTEGER_TYPE;
    def visitRange_arr(self,ctx:MPParser.Range_arrContext):
        if ctx.SUB() != None:
            return int('-' + ctx.INTEGER_TYPE().getText())
        else:
            return int(ctx.INTEGER_TYPE().getText())
    # func_decl_total: FUNCTION IDENTIFIER LB list_parameter? RB COLON (type_data | type_array) SEMI (var_decl_total)? compound_statement;
    def visitFunc_decl_total(self,ctx:MPParser.Func_decl_totalContext):
        param = []
        local = []
        if ctx.list_parameter() != None:
            param = self.visit(ctx.list_parameter())

        if ctx.var_decl_total() != None:
            local = self.visit(ctx.var_decl_total())

        cpstmt = self.visit(ctx.compound_statement())
        returntype = (self.visit(ctx.type_data()) if ctx.type_data() else self.visit(ctx.type_array()))
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),param,local,cpstmt,returntype)

    # list_parameter: parameter (SEMI parameter)*; 
    def visitList_parameter(self,ctx:MPParser.List_parameterContext):
        lstpara = []
        for x in ctx.parameter():
            lstpara += self.visit(x)

        return lstpara

    # parameter: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array);
    def visitParameter(self,ctx:MPParser.ParameterContext):
        if ctx.type_data()!= None:
            type_ = self.visit(ctx.type_data())
        else:
            type_ = self.visit(ctx.type_array())
        
        return [VarDecl(Id(x.getText()),type_) for x in ctx.IDENTIFIER()]
    
    # proc_decl_total: PROCEDURE IDENTIFIER LB list_parameter? RB SEMI (var_decl_total)? compound_statement;
    def visitProc_decl_total(self,ctx:MPParser.Proc_decl_totalContext):
        param = [] 
        local = []
        if ctx.list_parameter() != None:
            param = self.visit(ctx.list_parameter())

        if ctx.var_decl_total() != None:
            local = self.visit(ctx.var_decl_total())

        cpstmt = self.visit(ctx.compound_statement())
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),param,local,cpstmt)
    
    # statement: assignment_statement | if_statement | for_statement | while_statement | break_statement | continue_statement | return_statement | func_call_statement | compound_statement | with_statement;
    def visitStatement(self,ctx:MPParser.StatementContext):
        return self.visit(ctx.getChild(0))
    
    # assignment_statement: (lhs_assign ASSIGN)+ exp SEMI;
    def visitAssignment_statement(self,ctx:MPParser.Assignment_statementContext):
        # ol = ctx.lhs_assign()[::-1] # a = b = c = 4 -> ol = [c,b,a], tl = [c,b] 
        # tl = reversed(ctx.lhs_assign()[:1])
        # return [Assign(self.visit(x[0]),self.visit(x[1])) for x in zip(ol,[self.visit(ctx.exp())] + tl)]
        return reversed([Assign(self.visit(x),self.visit(y)) for x,y in zip(ctx.lhs_assign(),ctx.lhs_assign()[1:]+[ctx.exp()])])
        
    # lhs_assign: IDENTIFIER|index_express;
    def visitLhs_assign(self,ctx:MPParser.Lhs_assignContext):
        if ctx.IDENTIFIER() != None:
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.index_express())

    # if_statement: IF exp THEN statement (ELSE statement)?;
    def visitIf_statement(self,ctx:MPParser.If_statementContext):
        if ctx.ELSE() != None:
            return [If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))]
        else:
            return [If(self.visit(ctx.exp()),self.visit(ctx.statement(0)))]
        return 
    
    # while_statement: WHILE exp DO statement;
    def visitWhile_statement(self,ctx:MPParser.While_statementContext):
        return [While(self.visit(ctx.exp()),self.visit(ctx.statement()))]

    # for_statement: FOR IDENTIFIER ASSIGN exp (TO | DOWNTO) exp DO statement;
    def visitFor_statement(self,ctx:MPParser.For_statementContext):
        if ctx.TO() != None:
            booler = True
        else:
            booler = False

        return [For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),booler,self.visit(ctx.statement()))]

    # break_statement: BREAK SEMI;
    def visitBreak_statement(self,ctx:MPParser.Break_statementContext):
        return [Break()]

    # continue_statement: CONTINUE SEMI;
    def visitContinue_statement(self,ctx:MPParser.Continue_statementContext):
        return [Continue()]

    # return_statement: RETURN exp? SEMI;
    def visitReturn_statement(self,ctx:MPParser.Return_statementContext):
        if ctx.exp() != None:
            return [Return(self.visit(ctx.exp()))]
        else:
            return [Return()]

    # compound_statement: BEGIN statement* END;
    def visitCompound_statement(self,ctx:MPParser.Compound_statementContext):
        lststmt = []
        for x in ctx.statement():
            lststmt += self.visit(x)

        return lststmt

    # with_statement: WITH var_decl+ DO statement;
    def visitWith_statement(self,ctx:MPParser.With_statementContext):
        lstvar_decl = []
        for x in ctx.var_decl():
            lstvar_decl += self.visit(x)

        return [With(lstvar_decl,self.visit(ctx.statement()))]

    # func_call_statement: IDENTIFIER LB list_exp? RB SEMI ; // can xem lai
    def visitFunc_call_statement(self,ctx:MPParser.Func_call_statementContext):
        if ctx.list_exp() != None:
            return [CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_exp()))]
        else:
            return [CallStmt(Id(ctx.IDENTIFIER().getText()),[])]

    # list_exp: exp (COMMA exp)*;
    def visitList_exp(self,ctx:MPParser.List_expContext):
        lstexp = []
        for x in ctx.exp():
            exp_ = self.visit(x)
            if type(exp_) == type([]):
                lstexp = lstexp + exp_
            else:
                lstexp.append(exp_)

        return lstexp

    # exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1;  
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.AND() != None:
            return BinaryOp('andthen',self.visit(ctx.exp()),self.visit(ctx.exp1()))
        elif ctx.OR() != None:
            return BinaryOp('orelse',self.visit(ctx.exp()),self.visit(ctx.exp1()))
        else:
            return self.visit(ctx.exp1())

    # exp1: exp2 EQUAL exp2 | exp2 NOT_EQUAD exp2 | exp2 LESS_THAN exp2 | exp2 LESS_THAN_EQUAL exp2 | exp2 GREATER_THAN exp2 | exp2 GREATER_THAN_EQUAL exp2 | exp2;
    def visitExp1(self,ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
    
    # exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;
    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3()) 
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    # exp3: exp3 DIVISION exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;
    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4()) 
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))

    # exp4: NOT exp4 | SUB exp4 | exp5;
    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5()) 
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp4()))

    # exp5: literal | IDENTIFIER | func_call | LB exp RB | index_express; // con thieu??? element of an array or a function call.
    def visitExp5(self,ctx:MPParser.Exp5Context):
        if ctx.IDENTIFIER() != None:
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literal() != None:
            return self.visit(ctx.literal())
        elif ctx.func_call() != None:
            return self.visit(ctx.func_call())
        elif ctx.exp() != None:
            return self.visit(ctx.exp())
        else: 
            return self.visit(ctx.index_express())

    # index_express: (IDENTIFIER| func_call) LSB exp RSB;
    def visitIndex_express(self,ctx:MPParser.Index_expressContext):
        return ArrayCell(Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() != None else self.visit(ctx.func_call()),self.visit(ctx.exp()))

    # func_call: IDENTIFIER LB list_exp? RB;
    def visitFunc_call(self,ctx:MPParser.Func_callContext):
        if ctx.list_exp() != None:
            return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_exp()))
        else:
            return CallExpr(Id(ctx.IDENTIFIER().getText()),[])

    # literal: INTEGER_TYPE | REAL_TYPE | boolean_type | STRINGLIT;
    def visitLiteral(self,ctx:MPParser.LiteralContext):
        if ctx.INTEGER_TYPE() != None:
            return IntLiteral(int(ctx.INTEGER_TYPE().getText()))
        elif ctx.REAL_TYPE() != None:
            return FloatLiteral(float(ctx.REAL_TYPE().getText()))
        elif ctx.STRINGLIT() != None:
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.boolean_type())

    # boolean_type: TRUE | FALSE;
    def visitBoolean_type(self,ctx:MPParser.Boolean_typeContext):
        if ctx.TRUE() != None:
            return BooleanLiteral(True)
        else:
            return BooleanLiteral(False)

#####################################################-----END-----#####################################################
    # def visitProgram(self,ctx:MPParser.ProgramContext):
    #     return Program([self.visit(x) for x in ctx.decl()])

    # def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))

    # def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt)

    # def visitBody(self,ctx:MPParser.BodyContext):
    #     return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    # def visitStmt(self,ctx:MPParser.StmtContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self,ctx:MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self,ctx:MPParser.ExpContext):
    #     return IntLiteral(int(ctx.INTLIT().getText()))

    # def visitMtype(self,ctx:MPParser.MtypeContext):
    #     return IntType()
        
####################################################---THAM_KHAO---####################################################
    # def visitFundec(self, ctx:MPParser.FundecContext):
    #     param = []
    #     local = []
    #     if ctx.paralist() and ctx.vardec():
    #         param = self.visit(ctx.paralist())
    #         local = self.visit(ctx.vardec())
    #     elif ctx.paralist() and not(ctx.vardec()):
    #         param = self.visit(ctx.paralist())
    #         local = []
    #     elif not(ctx.paralist()) and ctx.vardec():
    #         param = []
    #         local = self.visit(ctx.vardec())
    #     elif not(ctx.paralist()) and not(ctx.vardec()):
    #         param = []
    #         local = []
    #     cpstmt = self.visit(ctx.compoundstate())
    #     returntype = self.visit(ctx.functiontype())
    #     return FuncDecl(Id(ctx.IDENT().getText()),param,local,cpstmt,returntype)

    # def visitProgram(self, ctx: MPParser.ProgramContext):
    #     lstdecl = []
    #     for x in ctx.declaration():
    #         decl = self.visit(x)
    #         if type(decl) == type([]):
    #             lstdecl = lstdecl + decl
    #         else:
    #             lstdecl.append(decl)
    #     return Program(lstdecl)

    # return reversed([Assign(self.visit(x),self.visit(y)) for x,y in zip(ctx.lhs(),ctx.lhs()[1:]+[ctx.exp()])])