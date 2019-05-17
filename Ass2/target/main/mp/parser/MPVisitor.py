# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decl_total.
    def visitVar_decl_total(self, ctx:MPParser.Var_decl_totalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decl.
    def visitVar_decl(self, ctx:MPParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#type_data.
    def visitType_data(self, ctx:MPParser.Type_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#type_array.
    def visitType_array(self, ctx:MPParser.Type_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_decl_total.
    def visitFunc_decl_total(self, ctx:MPParser.Func_decl_totalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_parameter.
    def visitList_parameter(self, ctx:MPParser.List_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parameter.
    def visitParameter(self, ctx:MPParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proc_decl_total.
    def visitProc_decl_total(self, ctx:MPParser.Proc_decl_totalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MPParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs_assign.
    def visitLhs_assign(self, ctx:MPParser.Lhs_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_statement.
    def visitIf_statement(self, ctx:MPParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_statement.
    def visitWhile_statement(self, ctx:MPParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_statement.
    def visitFor_statement(self, ctx:MPParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_statement.
    def visitBreak_statement(self, ctx:MPParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_statement.
    def visitContinue_statement(self, ctx:MPParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_statement.
    def visitReturn_statement(self, ctx:MPParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_statement.
    def visitCompound_statement(self, ctx:MPParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_statement.
    def visitWith_statement(self, ctx:MPParser.With_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_call_statement.
    def visitFunc_call_statement(self, ctx:MPParser.Func_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_exp.
    def visitList_exp(self, ctx:MPParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_express.
    def visitIndex_express(self, ctx:MPParser.Index_expressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_call.
    def visitFunc_call(self, ctx:MPParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boolean_type.
    def visitBoolean_type(self, ctx:MPParser.Boolean_typeContext):
        return self.visitChildren(ctx)



del MPParser