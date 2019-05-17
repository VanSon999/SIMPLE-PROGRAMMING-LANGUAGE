from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import *
class ASTGeneration(MPVisitor):
    #program : decl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])
        # return Program([y for x in ctx.decl() for y in self.visit(x)])

    #decl: var_decl_total | func_decl_total | proc_decl_total;
    def visitDecl(self,ctx:MPParser.DeclContext):
        return self.visit(ctx.getChild(0))

    #var_decl_total: VAR var_decl+;
    def visitVar_decl_total(self,ctx:MPParser.Var_decl_totalContext):
        return [seft.visit(x) for x in ctx.var_decl()]
        # return [y for x in ctx.var_decl() for y in self.visit(x)]

    #var_decl: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array) SEMI;
    def visitVar_decl(self,ctx:MPParser.Var_declContext):
        return [VarDecl(Id(i.gettext()),self.visit(ctx.type_data()) if ctx.type_data() else self.visit(ctx.type_array())) for i in ctx.IDENTIFIER()]

    #type_data: INTEGER | REAL | BOOLEAN | STRING;
    def visitType_data(self,ctx:MPParser.Type_dataContext):
        if (ctx.INTEGER()):
            return IntType()
        if (ctx.REAL()):
            return FloatType()
        if (ctx.BOOLEAN()):
            return BoolType()
        if (ctx.STRING):
            return StringType()

    #type_array: ARRAY LSB INTEGER_TYPE D_DOT INTEGER_TYPE RSB OF type_data;
    def visitType_array(self,ctx:MPParser.Type_arrayContext):
        return ArrayType(int(ctx.INTEGER_TYPE(0).getText()),int(ctx.INTEGER_TYPE(1).getText()),self.visit(ctx.type_data)) 

    #func_decl_total: FUNCTION IDENTIFIER LB list_parameter? RB COLON (type_data | type_array) SEMI (var_decl_total)? compound_statement;
    def visitFunc_decl_total(self,ctx:MPParser.Func_decl_totalContext): 
        param = []
        local = []   
        if ctx.list_parameter() :
            param = self.visit(list_parameter()) 

        if ctx.var_decl_total():
            local = self.visit(ctx.var_decl_total())

        if ctx.type_data():
            returnType = self.visit(ctx.type_data())

        else:
            returnType = self.visit(ctx.type_array()) 

        body = self.visit(ctx.compound_statement())
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), param,local,body, returnType)

    #proc_decl_total: PROCEDURE IDENTIFIER LB list_parameter? RB SEMI (var_decl_total)? compound_statement;
    def visitProc_decl_total(self,ctx:MPParser.Proc_decl_totalContext):
        param = []
        local = []   
        if ctx.list_parameter() :
            param = self.visit(list_parameter()) 

        if ctx.var_decl_total():
            local = self.visit(ctx.var_decl_total())

        body = self.visit(ctx.compound_statement())
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), param,local,body)

    #list_parameter: parameter (SEMI parameter)*;
    def visitList_parameter(self,ctx:MPParser.List_parameterContext):
        return [seft.visit(x) for x in ctx.parameter()]
        # return [y for x in ctx.parameter() for y in self.visit(x)]

    #parameter: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array);
    def visitParameter(self,ctx:MPParser.ParameterContext):
        return [VarDecl(Id(i.getText()),self.visit(ctx.type_data()) if ctx.type_data() else self.visit(ctx.type_array())) for i in ctx.IDENTIFIER()]

    #statement: assignment_statement | if_statement | for_statement | while_statement | break_statement | continue_statement | return_statement | func_call_statement | compound_statement | with_statement;
    def visitStatement(self,ctx:MPParser.StatementContext):  ########Note
        return self.visit(ctx.getChild(0))

    #assignment_statement: (lhs_assign ASSIGN)+ exp SEMI;
    def visitAssignment_statement(self,ctx:MPParser.Assignment_statementContext):
        tl = ctx.lhs_assign()[::-1] #danh sach lhs_assign dao nguoc vd: a := b :=c :=4 -> tl = [c,b,a] -> zip([c,b,a],[4] + [c,b])
        ol = reversed(ctx.lhs_assign()[1:])
        return [Assign(self.visit(x),self.visit(y)) for x,y in zip(tl,[self.visit(exp)] + ol)]

    #lhs_assign: IDENTIFIER|index_express;
    def visitLhs_assign(self,ctx:MPParser.Lhs_assignContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else: 
            return self.visit(ctx.index_express())
    #if_statement: IF exp THEN statement (ELSE statement)?;
    def visitIf_statement(self,ctx:MPParser.If_statementContext):
        if ctx.ELSE():
            return [If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))]
        else:
            return [If(self.visit(ctx.exp()),self.visit(ctx.statement(0)))]

    #while_statement: WHILE exp DO statement;
    def visitWhile_statement(self,ctx:MPParser.While_statementContext):
        return [While(self.visit(ctx.exp()),self.visit(ctx.statement()))]

    #for_statement: FOR IDENTIFIER ASSIGN exp (TO | DOWNTO) exp DO statement;
    def visitFor_statement(self,ctx:MPParser.For_statementContext):
        return [For(Id(ctx.IDENTIFIER().getText),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),True if ctx.TO() else False,self.visit(ctx.statement()))]

    #break_statement: BREAK SEMI;
    def visitBreak_statement(self,ctx:MPParser.Break_statementContext):
        return [Break()]

    #continue_statement: CONTINUE SEMI;
    def visitContinue_statement(self,ctx:MPParser.Continue_statementContext):
        return [Continue()]

    #return_statement: RETURN exp? SEMI;
    def visitReturn_statement(self,ctx:MPParser.Return_statementContext):
        return [Return(self.visit(ctx.exp()) if ctx.exp() else None)]

    #compound_statement: BEGIN statement* END;
    def visitCompound_statement(self,ctx:MPParser.Compound_statementContext):
        return [self.visit(x) for x in ctx.statement()]
    #with_statement: WITH var_decl+ DO statement;
    def visitWith_statement(self,ctx:MPParser.With_statementContext):
        return [With([seft.visit(x) for x in ctx.var_decl()],self.visit(ctx.statement()))]
        #return [With([y for x in ctx.var_decl() for y in self.visit(x)],self.visit(ctx.statement()))]

    #func_call_statement: IDENTIFIER LB list_exp? RB SEMI ; // can xem lai
    def visitFunc_call_statement(self,ctx:MPParser.Func_call_statementContext):
        if ctx.list_exp():
            return [CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_exp()))]
        else:
            return [CallStmt(Id(ctx.IDENTIFIER().getText()),[])]

    #list_exp: exp (COMMA exp)*;
    def visitList_exp(self,ctx:MPParser.List_expContext):
        return [self.visit(x) for x in ctx.exp()]

    #exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1;  
    def visitExp(self,ctx:MPParser.ExpContext):
        if (ctx.AND() and ctx.THEN()):
            return BinaryOp('andthen',self.visit(ctx.exp()),self.visit(ctx.exp1()))
        elif (ctx.OR() and ctx.ELSE()): 
            return BinaryOp('orelse',self.visit(ctx.exp()),self.visit(ctx.exp1()))
        else:
            return self.visit(ctx.exp1()) 

    #exp1: exp2 EQUAL exp2 | exp2 NOT_EQUAD exp2 | exp2 LESS_THAN exp2 | exp2 LESS_THAN_EQUAL exp2 | exp2 GREATER_THAN exp2 | exp2 GREATER_THAN_EQUAL exp2 | exp2;
    def visitExp1(self,ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.exp2(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1))) 

    #exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;
    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.exp3)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    #exp3: exp3 DIVISION exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;
    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.exp4)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))

    #exp4: NOT exp4 | SUB exp4 | exp5;
    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.exp5)
        else:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp4()))

    #exp5: literal | IDENTIFIER | func_call | LB exp RB | index_express; // con thieu??? element of an array or a function call.
    def visitExp5(self,ctx:MPParser.Exp5Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.index_express():
            return self.visit(ctx.index_express())
        else:
            return self.visit(ctx.exp())
        return 

    #literal: INTEGER_TYPE | REAL_TYPE | boolean_type | STRINGLIT;
    def visitLiteral(self,ctx:MPParser.LiteralContext):
        if ctx.INTEGER_TYPE():
            return IntLiteral(int(ctx.INTEGER_TYPE().getText()))
        elif ctx.REAL_TYPE():
            return FloatLiteral(float(ctx.REAL_TYPE().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.boolean_type())
    
    #boolean_type: TRUE | FALSE;
    def visitBoolean_type(self,ctx:MPParser.Boolean_typeContext):
        return BooleanLiteral('True') if ctx.TRUE() else BooleanLiteral('False')

    #index_express: (IDENTIFIER| func_call) LSB exp RSB;
    def visitIndex_express(self,ctx:MPParser.Index_expressContext):
        return ArrayCell(Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.func_call()),self.visit(ctx.exp()))

    #func_call: IDENTIFIER LB list_exp? RB;
    def visitFunc_call(self,ctx:MPParser.Func_callContext):
        return CallExpr(Id(ctx.IDENTIFIER()),self.visit(ctx.list_exp()) if ctx.list_exp() else [])

    # def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
    #     local,cpstmt = self.visit(ctx.body()) 
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))

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
        

    ###########################Tham khao##############################
    # def visitArray(self,ctx:MPParser.ArrayContext):
    #     return ArrayType(int(('-' if ctx.subop1() else '') + ctx.INTLIT(0).getText()),  #lower
    #                     int(('-' if ctx.subop2() else '') + ctx.INTLIT(1).getText()),   #upper
    #                     self.visit(ctx.primitivetype()))                                #eleType


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


    # def visitParalist(self, ctx:MPParser.ParalistContext):
    #     listvariable = [self.visit(x) for x in ctx.paradec()]
    #     return [i for x in listvariable for i in x]

    # def visitParadec(self, ctx:MPParser.ParadecContext):
    #     return [VarDecl(Id(x.getText()),self.visit(ctx.functiontype())) for x in ctx.IDENT()]

    # return reversed([Assign(self.visit(x),self.visit(y)) for x,y in zip(ctx.lhs(),ctx.lhs()[1:]+[ctx.exp()])])

    # [Assign(Id("c"),Id("exp")),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))]