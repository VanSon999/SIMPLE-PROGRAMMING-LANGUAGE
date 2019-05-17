# import unittest
# from TestUtils import TestAST
# from AST import *

# class ASTGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """procedure main(); begin end"""
#         expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
#         self.assertTrue(TestAST.test(input,expect,300))

#     def test_simple_function(self):
#         """More complex program"""
#         input = """function foo ():INTEGER; begin
#             putIntLn(4);
#         end"""
#         expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
#         self.assertTrue(TestAST.test(input,expect,301))
    
#     def test_call_without_parameter(self):
#         """More complex program"""
#         input = """procedure main (); begin
#             getIntLn();
#         end
#         function foo ():INTEGER; begin
#             putIntLn(4);
#         end"""
#         expect = str(Program([
#                 FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
#                 FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
#         self.assertTrue(TestAST.test(input,expect,302))
   
#     def test_call_without_parameter(self):
#         """More complex program"""
#         input = """procedure main(); 
# 	            begin
# 		            a := 3 - -4;
# 	            end"""
#         expect = str(Program([
#                 FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
#                 FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
#         self.assertTrue(TestAST.test(input,expect,302))

#     def test_simple_program12(self):
#         """Simple program: int main() {} """
#         input = """procedure main();
#                 begin
#                 a := true;
#             end"""
#         expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
#         self.assertTrue(TestAST.test(input,expect,314))

#     def test_simple_program14(self):
#         """Simple program: int main() {} """
#         input = """procedure main(a:INTEGER;b:real;c:real;d:boolean;e:boolean;f:boolean);
#                    var h:array[-1 .. -2] of real;
#                    begin
#                    end"""
#         expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
#         self.assertTrue(TestAST.test(input,expect,316))

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_var_decl_0(self):
        input = """var x: integer;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))
    def test_var_decl_1(self):
        input = """var x,y: integer;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    def test_var_decl_2(self):
        input = """var x,y,z: integer;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_var_decl_3(self):
        input = """var x: stRing;"""
        expect = str(Program([VarDecl(Id(r'x'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_var_decl_4(self):
        input = """var a,b,c,b,d: booLean;"""
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'd'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_var_decl_5(self):
        input = """var x: array [1 .. 2] of integer;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_var_decl_6(self):
        input = """var x,y: ArraY [1 .. 2] of reAl;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(1,2,FloatType())),VarDecl(Id(r'y'),ArrayType(1,2,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_var_decl_7(self):
        input = """var t: arraY [-1 .. 3] of sTring;"""
        expect = str(Program([VarDecl(Id(r't'),ArrayType(-1,3,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_var_decl_8(self):
        input = """var t,r: arraY [-1 .. 4] of integer;"""
        expect = str(Program([VarDecl(Id(r't'),ArrayType(-1,4,IntType())),VarDecl(Id(r'r'),ArrayType(-1,4,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_var_decl_9(self):
        input = """var e: array [3 .. -5] of integEr;"""
        expect = str(Program([VarDecl(Id(r'e'),ArrayType(-3,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_var_decl_10(self):
        input = """var x,v: arrAy [3 .. -8] of BoolEan;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-3,8,BoolType())),VarDecl(Id(r'v'),ArrayType(-3,8,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_var_decl_11(self):
        input = """var x,r,t,r: arrAy [3 .. -8] of BoolEan;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-3,8,BoolType())),VarDecl(Id(r'r'),ArrayType(-3,8,BoolType())),VarDecl(Id(r't'),ArrayType(-3,8,BoolType())),VarDecl(Id(r'r'),ArrayType(-3,8,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_var_decl_12(self):
        input = """var x: arrAy [-2 .. -5] of String;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-2,-5,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,312))
    def test_var_decl_13(self):
        input = """var x,t: arrAy [-2 .. -5] of string;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-2,-5,StringType())),VarDecl(Id(r't'),ArrayType(-2,-5,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_var_decl_14(self):
        input = """var x,r,e,s: arrAy [-3 .. -3] of reaL;"""
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-3,-3,FloatType())),VarDecl(Id(r'r'),ArrayType(-3,-3,FloatType())),VarDecl(Id(r'e'),ArrayType(-3,-3,FloatType())),VarDecl(Id(r's'),ArrayType(-3,-3,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_var_decl_15(self):
        input = """var x: integer;
                        w,e: string;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'w'),StringType()),VarDecl(Id(r'e'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_var_decl_16(self):
        input = """var x: integer;
                        e,t,r,w: array [3 .. 4] of string;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'e'),ArrayType(3,4,StringType())),VarDecl(Id(r't'),ArrayType(3,4,StringType())),VarDecl(Id(r'r'),ArrayType(3,4,StringType())),VarDecl(Id(r'w'),ArrayType(3,4,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_var_decl_17(self):
        input = """var x: integer;
                        a: string;
                        y: real;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'y'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_var_decl_18(self):
        input = """var x: integer;
                    var d,f: array [5 .. -9] of real;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'd'),ArrayType(-5,9,FloatType())),VarDecl(Id(r'f'),ArrayType(-5,9,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_var_decl_19(self):
        input = """var x: integer;
                    var e: string;
                    var w: arrAy [1 .. 2] of integer;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'e'),StringType()),VarDecl(Id(r'w'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_func_decl_20(self):
        input = """function main(): integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_func_decl_21(self):
        input = """function hello(): StrinG;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'hello'),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test_func_decl_22(self):
        input = """function hello(): BoOlEaN;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'hello'),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_func_decl_23(self):
        input = """function my_name(): ReaL;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'my_name'),[],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_func_decl_24(self):
        input = """function my_name_no(): arraY [-9 .. 7] of integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'my_name_no'),[],[],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_func_decl_25(self):
        input = """function main(): integer;
                var a,b,c: integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_func_decl_26(self):
        input = """function main_2(): arraY [-9 .. 7] of integer;
                var hello: array [4 .. 5] of sTring;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_2'),[],[VarDecl(Id(r'hello'),ArrayType(4,5,StringType()))],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_func_decl_26(self):
        input = """function main_2(): arraY [-9 .. 7] of integer;
                var hello: array [4 .. 5] of sTring;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_2'),[],[VarDecl(Id(r'hello'),ArrayType(4,5,StringType()))],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_func_decl_27(self):
        input = """function main_2(): arraY [-9 .. 7] of integer;
                var hello: array [4 .. 5] of sTring;
                    bye: strIng;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_2'),[],[VarDecl(Id(r'hello'),ArrayType(4,5,StringType())),VarDecl(Id(r'bye'),StringType())],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_func_decl_28(self):
        input = """function main_2(): arraY [-9 .. 7] of integer;
                var hello,gelly: integer;
                    bye,r4: strIng;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_2'),[],[VarDecl(Id(r'hello'),IntType()),VarDecl(Id(r'gelly'),IntType()),VarDecl(Id(r'bye'),StringType()),VarDecl(Id(r'r4'),StringType())],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_func_decl_29(self):
        input = """function main_2(): arraY [-9 .. 7] of integer;
                var hello,gelly: integer;
                    bye,r4: strIng;
                    rere: booLean;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_2'),[],[VarDecl(Id(r'hello'),IntType()),VarDecl(Id(r'gelly'),IntType()),VarDecl(Id(r'bye'),StringType()),VarDecl(Id(r'r4'),StringType()),VarDecl(Id(r'rere'),BoolType())],[],ArrayType(-9,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_func_decl_30(self):
        input = """function main(a:integer): integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_func_decl_31(self):
        input = """function main(a,b,c: integer): integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_func_decl_32(self):
        input = """function main(a: integer;b: string): integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_func_decl_33(self):
        input = """function main(a,b: integer;c: string;d,e: array [5 .. 6] of booLean): integer;
                var a,b,c: integer;
                    e,f: booLean;
                    e: array [1 .. 2] of string;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),ArrayType(5,6,BoolType())),VarDecl(Id(r'e'),ArrayType(5,6,BoolType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'e'),ArrayType(1,2,StringType()))],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_func_decl_34(self):
        input = """function final(r4: boolEan;a,b: integer;c: string;d,e: array [5 .. 6] of booLean): Array [-4 .. 6] of string;
                var a,b,c: integer;
                    e,f: booLean;
                    e: array [1 .. 2] of string;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'final'),[VarDecl(Id(r'r4'),BoolType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),ArrayType(5,6,BoolType())),VarDecl(Id(r'e'),ArrayType(5,6,BoolType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'e'),ArrayType(1,2,StringType()))],[],ArrayType(-4,6,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_proc_decl_35(self):
        input = """procedure main();
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_proc_decl_36(self):
        input = """procedure hello();
                var a: real;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'hello'),[],[VarDecl(Id(r'a'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_proc_decl_37(self):
        input = """procedure hello_2();
                var a,b,c: real;
                    fe: array [6 .. 7] of String;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'hello_2'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'fe'),ArrayType(6,7,StringType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_proc_decl_38(self):
        input = """procedure hello_2();
                var a,b,c: real;
                    fe,cu,al: array [6 .. 7] of String;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'hello_2'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'fe'),ArrayType(6,7,StringType())),VarDecl(Id(r'cu'),ArrayType(6,7,StringType())),VarDecl(Id(r'al'),ArrayType(6,7,StringType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_proc_decl_39(self):
        input = """procedure proc_decl();
                var a,b,c: real;
                    fe: array [6 .. 7] of String;
                    df: integer;
                    le: booLean;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'fe'),ArrayType(6,7,StringType())),VarDecl(Id(r'df'),IntType()),VarDecl(Id(r'le'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_proc_decl_40(self):
        input = """procedure main(a: integer);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_proc_decl_41(self):
        input = """procedure proc_decl(a,b: integer);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_proc_decl_42(self):
        input = """procedure self_42(a,b: integer; c,d: String);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'self_42'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_proc_decl_43(self):
        input = """procedure AST(a: integer;b,c: String;d: arraY[4 .. 5] of integer);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'AST'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),ArrayType(4,5,IntType()))],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_proc_decl_44(self):
        input = """procedure proc_decl(a: integer;b: String; c: Real; d: BoolEan; e: array [5 .. 6] of BooLean);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),ArrayType(5,6,BoolType()))],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_proc_decl_45(self):
        input = """procedure proc_decl(a: integer);
                var a: integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'a'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_proc_decl_46(self):
        input = """procedure main(a,v: integer);
                var x,y: String;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'v'),IntType())],[VarDecl(Id(r'x'),StringType()),VarDecl(Id(r'y'),StringType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_proc_decl_47(self):
        input = """procedure proc_decl(a: integer;b: String);
                var a: integer;
                    b: String;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_proc_decl_48(self):
        input = """procedure proc_decl(a,b: integer;c,d: String);
                var a,r: array [5 .. 6] of string;
                    r,e: array [7 .. 8] of integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),StringType())],[VarDecl(Id(r'a'),ArrayType(5,6,StringType())),VarDecl(Id(r'r'),ArrayType(5,6,StringType())),VarDecl(Id(r'r'),ArrayType(7,8,IntType())),VarDecl(Id(r'e'),ArrayType(7,8,IntType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_proc_decl_49(self):
        input = """procedure proc_decl(a: integer;b: String; c: Real; d: BoolEan; e: array [5 .. 6] of BooLean);
                var a: integer;
                    b: String; 
                    c: Real; 
                    d: BoolEan; 
                    e: array [5 .. 6] of BooLean;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proc_decl'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),ArrayType(5,6,BoolType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),ArrayType(5,6,BoolType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_exp_decl_50(self):
        input = """procedure main();
                begin
                    A := 4 and then 3;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'andthen',IntLiteral(4),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_exp_decl_51(self):
        input = """procedure main();
                begin
                    A := 4 >= 3;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'>=',IntLiteral(4),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_exp_decl_52(self):
        input = """procedure main();
                begin
                    A := a[3] - a[2];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'-',ArrayCell(Id(r'a'),IntLiteral(3)),ArrayCell(Id(r'a'),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_exp_decl_53(self):
        input = """procedure main();
                begin
                    A := a[3] / call(3);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'/',ArrayCell(Id(r'a'),IntLiteral(3)),CallExpr(Id(r'call'),[IntLiteral(3)])))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_exp_decl_54(self):
        input = """procedure main();
                begin
                    A := - (True);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),UnaryOp(r'-',BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_exp_decl_55(self):
        input = """procedure main();
                begin
                    A := ((f + 2) * (3 - 4) / 45) and then 34;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'andthen',BinaryOp(r'/',BinaryOp(r'*',BinaryOp(r'+',Id(r'f'),IntLiteral(2)),BinaryOp(r'-',IntLiteral(3),IntLiteral(4))),IntLiteral(45)),IntLiteral(34)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_exp_decl_56(self):
        input = """procedure main();
                begin
                    A := 3.456 - (true + call_stmt(45,56,67)) or else fa[5];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'orelse',BinaryOp(r'-',FloatLiteral(3.456),BinaryOp(r'+',BooleanLiteral(True),CallExpr(Id(r'call_stmt'),[IntLiteral(45),IntLiteral(56),IntLiteral(67)]))),ArrayCell(Id(r'fa'),IntLiteral(5))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_exp_decl_57(self):
        input = """procedure main();
                begin
                    A := 4.22 >= 3 + 4 * 5 and not 2;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'>=',FloatLiteral(4.22),BinaryOp(r'+',IntLiteral(3),BinaryOp(r'and',BinaryOp(r'*',IntLiteral(4),IntLiteral(5)),UnaryOp(r'not',IntLiteral(2))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,357))
    
    def test_exp_decl_58(self):
        input = """procedure main();
                begin
                    A := "hello_string" + "hello_string_2";
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'+',StringLiteral(r'hello_string'),StringLiteral(r'hello_string_2')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_exp_decl_59(self):
        input = """procedure main();
                begin
                    A := halo - "ghi" mod (5 - 6) / not call(4,5 + 6,"hello" * ("h" - "6"));
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'-',Id(r'halo'),BinaryOp(r'/',BinaryOp(r'mod',StringLiteral(r'ghi'),BinaryOp(r'-',IntLiteral(5),IntLiteral(6))),UnaryOp(r'not',CallExpr(Id(r'call'),[IntLiteral(4),BinaryOp(r'+',IntLiteral(5),IntLiteral(6)),BinaryOp(r'*',StringLiteral(r'hello'),BinaryOp(r'-',StringLiteral(r'h'),StringLiteral(r'6')))])))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_exp_decl_60(self):
        input = """procedure main();
                begin
                    A:= id[3 + 2 * 5 - 1];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),ArrayCell(Id(r'id'),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(3),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),IntLiteral(1))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_exp_decl_61(self):
        input = """procedure main();
                begin
                    A:= call_stmt(call_2(4,5))[True and then "hello" + 3e-2];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),ArrayCell(CallExpr(Id(r'call_stmt'),[CallExpr(Id(r'call_2'),[IntLiteral(4),IntLiteral(5)])]),BinaryOp(r'andthen',BooleanLiteral(True),BinaryOp(r'+',StringLiteral(r'hello'),FloatLiteral(3e-2)))))])]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_exp_decl_62(self):
        input = """procedure main();
                begin
                    foo[3] := 10 + call(10)[45] - re[2222];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(Id(r'foo'),IntLiteral(3)),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(10),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(10)]),IntLiteral(45))),ArrayCell(Id(r're'),IntLiteral(2222))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_exp_decl_63(self):
        input = """procedure main();
                begin
                    A := call_1(0)[call_2(0)[call_3(0)[final]]];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),ArrayCell(CallExpr(Id(r'call_1'),[IntLiteral(0)]),ArrayCell(CallExpr(Id(r'call_2'),[IntLiteral(0)]),ArrayCell(CallExpr(Id(r'call_3'),[IntLiteral(0)]),Id(r'final')))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_exp_decl_64(self):
        input = """procedure main();
                begin
                    A := call(3,4,5,5,6,6,6,6,66)[re[3] >= 45];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(5),IntLiteral(6),IntLiteral(6),IntLiteral(6),IntLiteral(6),IntLiteral(66)]),BinaryOp(r'>=',ArrayCell(Id(r're'),IntLiteral(3)),IntLiteral(45))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_exp_decl_65(self):
        input = """procedure main();
                begin
                    A:= call(3,call(3,call(3,call(3))));
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),CallExpr(Id(r'call'),[IntLiteral(3),CallExpr(Id(r'call'),[IntLiteral(3),CallExpr(Id(r'call'),[IntLiteral(3),CallExpr(Id(r'call'),[IntLiteral(3)])])])]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_exp_decl_66(self):
        input = """procedure main();
                begin
                    A := call(3,4,5,5,6,6,6,6,66)[re[3] >= 45];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(5),IntLiteral(6),IntLiteral(6),IntLiteral(6),IntLiteral(6),IntLiteral(66)]),BinaryOp(r'>=',ArrayCell(Id(r're'),IntLiteral(3)),IntLiteral(45))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_exp_decl_67(self):
        input = """procedure main();
                begin
                    A := call(call(3)[call(3,re[final(5,6,6,6,6)])]);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),CallExpr(Id(r'call'),[ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3)]),CallExpr(Id(r'call'),[IntLiteral(3),ArrayCell(Id(r're'),CallExpr(Id(r'final'),[IntLiteral(5),IntLiteral(6),IntLiteral(6),IntLiteral(6),IntLiteral(6)]))]))]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_exp_decl_68(self):
        input = """procedure main();
                begin
                    A := call();
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),CallExpr(Id(r'call'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_exp_decl_69(self):
        input = """procedure main();
                begin
                    A := hello() + hello(33);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'+',CallExpr(Id(r'hello'),[]),CallExpr(Id(r'hello'),[IntLiteral(33)])))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))\
    
    def test_stmt_decl_70(self):
        input = """procedure main();
                begin
                    A := foo[3] := B := call(3)[45] := 2 + 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3)]),IntLiteral(45)),BinaryOp(r'+',IntLiteral(2),IntLiteral(4))),Assign(Id(r'B'),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3)]),IntLiteral(45))),Assign(ArrayCell(Id(r'foo'),IntLiteral(3)),Id(r'B')),Assign(Id(r'A'),ArrayCell(Id(r'foo'),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_stmt_decl_71(self):
        input = """procedure main();
                begin
                    call(4,5,6)[45] := hello := bo := 8 * 9 - 10 + 3;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'bo'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'*',IntLiteral(8),IntLiteral(9)),IntLiteral(10)),IntLiteral(3))),Assign(Id(r'hello'),Id(r'bo')),Assign(ArrayCell(CallExpr(Id(r'call'),[IntLiteral(4),IntLiteral(5),IntLiteral(6)]),IntLiteral(45)),Id(r'hello'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_stmt_decl_72(self):
        input = """procedure main();
                begin
                    if 2 > 3 then a := 2;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',IntLiteral(2),IntLiteral(3)),[Assign(Id(r'a'),IntLiteral(2))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
    def test_stmt_decl_73(self):
        input = """procedure main();
                begin
                    if 2 > 3 then a := 2; else a:= 1;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',IntLiteral(2),IntLiteral(3)),[Assign(Id(r'a'),IntLiteral(2))],[Assign(Id(r'a'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_stmt_decl_74(self):
        input = """procedure main();
                begin
                    while (2 * 4 - 3 <= 5) and then 2 Do
                    Begin
                        Hello := call(3)[4];
                    End
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[While(BinaryOp(r'andthen',BinaryOp(r'<=',BinaryOp(r'-',BinaryOp(r'*',IntLiteral(2),IntLiteral(4)),IntLiteral(3)),IntLiteral(5)),IntLiteral(2)),[Assign(Id(r'Hello'),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(3)]),IntLiteral(4)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_stmt_decl_75(self):
        input = """procedure main();
                begin
                    WHILE 22222 + call(3) = 4 do fdd[3] := gf[4] := 5;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[While(BinaryOp(r'=',BinaryOp(r'+',IntLiteral(22222),CallExpr(Id(r'call'),[IntLiteral(3)])),IntLiteral(4)),[Assign(ArrayCell(Id(r'gf'),IntLiteral(4)),IntLiteral(5)),Assign(ArrayCell(Id(r'fdd'),IntLiteral(3)),ArrayCell(Id(r'gf'),IntLiteral(4)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_stmt_decl_76(self):
        input = """procedure main();
                begin
                    break;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Break()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_stmt_decl_77(self):
        input = """procedure main();
                begin
                    continue;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Continue()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_stmt_decl_78(self):
        input = """procedure main();
                begin
                    return;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_stmt_decl_79(self):
        input = """procedure main();
                begin
                    return hello >= 3 + 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Return(BinaryOp(r'>=',Id(r'hello'),BinaryOp(r'+',IntLiteral(3),IntLiteral(4))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_stmt_decl_80(self):
        input = """procedure main();
                begin
                    begin
                        a := 4;
                        b := 5;
                        c := 6;
                        begin
                            d := 7;
                            e := 8;
                        end
                    end
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(4)),Assign(Id(r'b'),IntLiteral(5)),Assign(Id(r'c'),IntLiteral(6)),Assign(Id(r'd'),IntLiteral(7)),Assign(Id(r'e'),IntLiteral(8))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_stmt_decl_81(self):
        input = """procedure main();
                begin
                    begin
                        begin
                            begin
                                begin
                                    a := 6;
                                end
                            end
                        end
                    end
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType())],[Assign(Id(r'hello'),Id(r'may_con_quy'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_stmt_decl_81(self):
        input = """procedure main();
                begin
                    with a:integer; do
                        hello := may_con_quy;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType())],[Assign(Id(r'hello'),Id(r'may_con_quy'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_stmt_decl_82(self):
        input = """procedure main();
                begin
                    with a:integer;b:array [1 .. 2] of boolean; do
                        hello := may_con_quy;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),ArrayType(1,2,BoolType()))],[Assign(Id(r'hello'),Id(r'may_con_quy'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_stmt_decl_83(self):
        input = """procedure main();
                begin
                    hello(4,5,c,3 + c,1111 and then 4);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'hello'),[IntLiteral(4),IntLiteral(5),Id(r'c'),BinaryOp(r'+',IntLiteral(3),Id(r'c')),BinaryOp(r'andthen',IntLiteral(1111),IntLiteral(4))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_stmt_decl_84(self):
        input = """procedure main();
                begin
                    hello_may_cung(3 / 2,55);
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'hello_may_cung'),[BinaryOp(r'/',IntLiteral(3),IntLiteral(2)),IntLiteral(55)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_stmt_decl_85(self):
        input = """procedure main();
                begin
                    if 4 > 5 then
                        q := 3;
                    while i < 100 do
                        i := i + 1;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',IntLiteral(4),IntLiteral(5)),[Assign(Id(r'q'),IntLiteral(3))],[]),While(BinaryOp(r'<',Id(r'i'),IntLiteral(100)),[Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_stmt_decl_86(self):
        input = """procedure main(x,g: integer);
                var r: integer;
                begiN
                    while r > 45 do
                        g := 78;
                enD
                function j(): string;
                var _2: integer;
                begiN   
                    while a + a > 45 do
                        foo(3)[3] := 45;
                    while 3 > 4 do
                        fg[45] := 78;
                enD"""
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'g'),IntType())],[VarDecl(Id(r'r'),IntType())],[While(BinaryOp(r'>',Id(r'r'),IntLiteral(45)),[Assign(Id(r'g'),IntLiteral(78))])],VoidType()),FuncDecl(Id(r'j'),[],[VarDecl(Id(r'_2'),IntType())],[While(BinaryOp(r'>',BinaryOp(r'+',Id(r'a'),Id(r'a')),IntLiteral(45)),[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),IntLiteral(3)),IntLiteral(45))]),While(BinaryOp(r'>',IntLiteral(3),IntLiteral(4)),[Assign(ArrayCell(Id(r'fg'),IntLiteral(45)),IntLiteral(78))])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_stmt_decl_87(self):
        input = """procedurE foo (b : real) ;
                var a : array [2 .. 3] of integer;
                    b: string;
                    e: real;
                    f: boolean;
                begin
                    while(a=4) do
                        with a,b,c:integer;b: array [1 .. 3] of StRing; do 
                            while(a=4) do
                                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                                    e:=4;
                End"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(4))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))
    def test_stmt_decl_88(self):
        input = """procedurE foo (b : real);
                var a : array [2 .. 3] of integer;
                    b: string;
                    e: real;
                    f: boolean;
                begin
                    while (a=4) do
                        for i:=4 to 5 do
                            while(a=4) do
                                for i:=4 to 6+(7+(4+3)) do
                                    while(a=4) do
                                        for i:=4 to a do
                                            while(a=4) do
                                                for i:=4 to 5 do
                                                    while(a=4) do
                                                        for i:=4 to l do
                                                            a:=4;
                End"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'a'),ArrayType(2,3,IntType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),BoolType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[For(Id(r'i'),IntLiteral(4),IntLiteral(5),True,[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[For(Id(r'i'),IntLiteral(4),BinaryOp(r'+',IntLiteral(6),BinaryOp(r'+',IntLiteral(7),BinaryOp(r'+',IntLiteral(4),IntLiteral(3)))),True,[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[For(Id(r'i'),IntLiteral(4),Id(r'a'),True,[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[For(Id(r'i'),IntLiteral(4),IntLiteral(5),True,[While(BinaryOp(r'=',Id(r'a'),IntLiteral(4)),[For(Id(r'i'),IntLiteral(4),Id(r'l'),True,[Assign(Id(r'a'),IntLiteral(4))])])])])])])])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_stmt_decl_89(self):
        input = """procedure foo();
                var x, y: integer;
                begin
                    x := y*12 div 100 mod 10;
                    write("Please type the first char: ");
                    readln(c1);
                    write("Please type the second one: ");
                    readln(c2);
                    if (upcase(c1)=lowercase(c1 div 12)) then
                        writeln("The first char is not a letter");
                    else if (upcase(c2)=lowercase(c2)) then
                        writeln("The second char is not a letter");
                    else if (upcase(c1)>upcase(c2)) then
                        writeln("The first letter is [",c2,"] while the second is [",c1,"].");
                    else
                        writeln("The first letter is [,c1,] while the second is [",c2,"].");
                end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[Assign(Id(r'x'),BinaryOp(r'mod',BinaryOp(r'div',BinaryOp(r'*',Id(r'y'),IntLiteral(12)),IntLiteral(100)),IntLiteral(10))),CallStmt(Id(r'write'),[StringLiteral(r'Please type the first char: ')]),CallStmt(Id(r'readln'),[Id(r'c1')]),CallStmt(Id(r'write'),[StringLiteral(r'Please type the second one: ')]),CallStmt(Id(r'readln'),[Id(r'c2')]),If(BinaryOp(r'=',CallExpr(Id(r'upcase'),[Id(r'c1')]),CallExpr(Id(r'lowercase'),[BinaryOp(r'div',Id(r'c1'),IntLiteral(12))])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The first char is not a letter')])],[If(BinaryOp(r'=',CallExpr(Id(r'upcase'),[Id(r'c2')]),CallExpr(Id(r'lowercase'),[Id(r'c2')])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The second char is not a letter')])],[If(BinaryOp(r'>',CallExpr(Id(r'upcase'),[Id(r'c1')]),CallExpr(Id(r'upcase'),[Id(r'c2')])),[CallStmt(Id(r'writeln'),[StringLiteral(r'The first letter is ['),Id(r'c2'),StringLiteral(r'] while the second is ['),Id(r'c1'),StringLiteral(r'].')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'The first letter is [,c1,] while the second is ['),Id(r'c2'),StringLiteral(r'].')])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_stmt_decl_90(self):
        input = """function main(): string;
                begin
                    return a + 4;
                end
                procedure main();
                begin
                    for a:= we * 4 / 3 to f + 4 * 8 mod 3 do
                        if (2 = 3) then
                            return a / 2 and d + 3 > a or else 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Return(BinaryOp(r'+',Id(r'a'),IntLiteral(4)))],StringType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),BinaryOp(r'/',BinaryOp(r'*',Id(r'we'),IntLiteral(4)),IntLiteral(3)),BinaryOp(r'+',Id(r'f'),BinaryOp(r'mod',BinaryOp(r'*',IntLiteral(4),IntLiteral(8)),IntLiteral(3))),True,[If(BinaryOp(r'=',IntLiteral(2),IntLiteral(3)),[Return(BinaryOp(r'orelse',BinaryOp(r'>',BinaryOp(r'+',BinaryOp(r'and',BinaryOp(r'/',Id(r'a'),IntLiteral(2)),Id(r'd')),IntLiteral(3)),Id(r'a')),IntLiteral(4)))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_stmt_decl_91(self):
        input = """function main(): string;
                begin
                    return a + 4;
                end
                procedure main();
                begin
                    for a:= we * 4 / 3 to f + 4 * 8 mod 3 do
                        if (2 = 3) then
                            return a / 2 and d + 3 > a or else 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Return(BinaryOp(r'+',Id(r'a'),IntLiteral(4)))],StringType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),BinaryOp(r'/',BinaryOp(r'*',Id(r'we'),IntLiteral(4)),IntLiteral(3)),BinaryOp(r'+',Id(r'f'),BinaryOp(r'mod',BinaryOp(r'*',IntLiteral(4),IntLiteral(8)),IntLiteral(3))),True,[If(BinaryOp(r'=',IntLiteral(2),IntLiteral(3)),[Return(BinaryOp(r'orelse',BinaryOp(r'>',BinaryOp(r'+',BinaryOp(r'and',BinaryOp(r'/',Id(r'a'),IntLiteral(2)),Id(r'd')),IntLiteral(3)),Id(r'a')),IntLiteral(4)))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_stmt_decl_92(self):
        input = """procedure change(y : integer);
                begin
                    y := 1;	
                    x := 0;
                    writeln(x);
                    change(x);
                    writeln(x);
                    change(2 + 5); (* Allows expressions *)
                end"""
        expect = str(Program([FuncDecl(Id(r'change'),[VarDecl(Id(r'y'),IntType())],[],[Assign(Id(r'y'),IntLiteral(1)),Assign(Id(r'x'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[Id(r'x')]),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[BinaryOp(r'+',IntLiteral(2),IntLiteral(5))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_stmt_decl_93(self):
        input = """var n : integer;
                function power2(n:integer): integer;
                var k : integer;
                begin
                    k := 0;
                    while (n mod 2 = 0) do
                    begin
                        k := succ(k);
                        n := n div 2;
                    end
                    power2 := k;
                end"""
        expect = str(Program([VarDecl(Id(r'n'),IntType()),FuncDecl(Id(r'power2'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'k'),IntType())],[Assign(Id(r'k'),IntLiteral(0)),While(BinaryOp(r'=',BinaryOp(r'mod',Id(r'n'),IntLiteral(2)),IntLiteral(0)),[Assign(Id(r'k'),CallExpr(Id(r'succ'),[Id(r'k')])),Assign(Id(r'n'),BinaryOp(r'div',Id(r'n'),IntLiteral(2)))]),Assign(Id(r'power2'),Id(r'k'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_stmt_decl_94(self):
        input = """function isPrime(n : integer) : boolean;
                var
                    soFarPrime : boolean;
                    candidate : integer;
                begin
                    soFarPrime := TRUE;

                    for candidate := 2 to (n - 1) do
                        if (n mod candidate = 0) then
                            soFarPrime := FALSE;
                    isPrime := soFarPrime;
                end"""
        expect = str(Program([FuncDecl(Id(r'isPrime'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'soFarPrime'),BoolType()),VarDecl(Id(r'candidate'),IntType())],[Assign(Id(r'soFarPrime'),BooleanLiteral(True)),For(Id(r'candidate'),IntLiteral(2),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'n'),Id(r'candidate')),IntLiteral(0)),[Assign(Id(r'soFarPrime'),BooleanLiteral(False))],[])]),Assign(Id(r'isPrime'),Id(r'soFarPrime'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_stmt_decl_95(self):
        input = """procedure addrationals(num1, den1 : integer; num2, den2 : integer);
                begin
                    num1 := num1 * den2 + num2 * den1;
                    den1 := den1 * den2;
                    read(n1, d1);
                    read(n2, d2);
                    addrationals(n1, d1, n2, d2);
                    writeln(n1, d1);
                end"""
        expect = str(Program([FuncDecl(Id(r'addrationals'),[VarDecl(Id(r'num1'),IntType()),VarDecl(Id(r'den1'),IntType()),VarDecl(Id(r'num2'),IntType()),VarDecl(Id(r'den2'),IntType())],[],[Assign(Id(r'num1'),BinaryOp(r'+',BinaryOp(r'*',Id(r'num1'),Id(r'den2')),BinaryOp(r'*',Id(r'num2'),Id(r'den1')))),Assign(Id(r'den1'),BinaryOp(r'*',Id(r'den1'),Id(r'den2'))),CallStmt(Id(r'read'),[Id(r'n1'),Id(r'd1')]),CallStmt(Id(r'read'),[Id(r'n2'),Id(r'd2')]),CallStmt(Id(r'addrationals'),[Id(r'n1'),Id(r'd1'),Id(r'n2'),Id(r'd2')]),CallStmt(Id(r'writeln'),[Id(r'n1'),Id(r'd1')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_stmt_decl_96(self):
        input = """procedure average();
                var
                    count : integer;
                    sum, current : real;
                    avg : real;
                begin
                    current := 0.0;
                    sum := 0.0;
                    count := 0;
                    while current <> END_OF_DATA do
                    begin
                        read(current);
                        sum := sum + current;
                        count := succ(count);		
                    end
                    avg := sum / (count + 0.0);
                    writeln("AVERAGE:", avg);
                end
                var a: integer;
                var f,b,g,d: array [1 .. 3] of integer;"""
        expect = str(Program([FuncDecl(Id(r'average'),[],[VarDecl(Id(r'count'),IntType()),VarDecl(Id(r'sum'),FloatType()),VarDecl(Id(r'current'),FloatType()),VarDecl(Id(r'avg'),FloatType())],[Assign(Id(r'current'),FloatLiteral(0.0)),Assign(Id(r'sum'),FloatLiteral(0.0)),Assign(Id(r'count'),IntLiteral(0)),While(BinaryOp(r'<>',Id(r'current'),Id(r'END_OF_DATA')),[CallStmt(Id(r'read'),[Id(r'current')]),Assign(Id(r'sum'),BinaryOp(r'+',Id(r'sum'),Id(r'current'))),Assign(Id(r'count'),CallExpr(Id(r'succ'),[Id(r'count')]))]),Assign(Id(r'avg'),BinaryOp(r'/',Id(r'sum'),BinaryOp(r'+',Id(r'count'),FloatLiteral(0.0)))),CallStmt(Id(r'writeln'),[StringLiteral(r'AVERAGE:'),Id(r'avg')])],VoidType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'f'),ArrayType(1,3,IntType())),VarDecl(Id(r'b'),ArrayType(1,3,IntType())),VarDecl(Id(r'g'),ArrayType(1,3,IntType())),VarDecl(Id(r'd'),ArrayType(1,3,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_stmt_decl_97(self):
        input = """procedure main(); 
                begin
                    for a:=1 to 2 do a:=3;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),IntLiteral(1),IntLiteral(2),True,[Assign(Id(r'a'),IntLiteral(3))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_stmt_decl_98(self):
        input = """function hello(a,b:real; c:integer): integer; 
                var name: string; 
                begin
                end
                procedure goodbye();
                var name: string; 
                begin
                end
                procedure main();
                begin
                    hello(a,b,c);
                end"""
        expect = str(Program([FuncDecl(Id(r'hello'),[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),IntType())],[VarDecl(Id(r'name'),StringType())],[],IntType()),FuncDecl(Id(r'goodbye'),[],[VarDecl(Id(r'name'),StringType())],[],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'hello'),[Id(r'a'),Id(r'b'),Id(r'c')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_stmt_decl_99(self):
        input = """procedure main(); 
                begin
                    if a then f[a] := 4; else begin
                        for a:= 5 downto 1 do begin
                            if a > 3 then continue; else break;
                        end
                    end
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(Id(r'a'),[Assign(ArrayCell(Id(r'f'),Id(r'a')),IntLiteral(4))],[For(Id(r'a'),IntLiteral(5),IntLiteral(1),False,[If(BinaryOp(r'>',Id(r'a'),IntLiteral(3)),[Continue()],[Break()])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))