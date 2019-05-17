import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_pro_1_AST1(self):
        input = """var a:integer;
                b,c:real;
                procedure in();
                begin
                end"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),FuncDecl(Id(r'in'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_var_pro_2_AST2(self):
        """Simple program: int main() {} """
        input = """var t:array [-5 .. -6] of Integer;
                procedure in();
                begin
                end
                var y,x:array [-1 .. -2] of String;"""
        expect = str(Program([VarDecl(Id(r't'),ArrayType(-5,-6,IntType())),FuncDecl(Id(r'in'),[],[],[],VoidType()),VarDecl(Id(r'y'),ArrayType(-1,-2,StringType())),VarDecl(Id(r'x'),ArrayType(-1,-2,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_pro_param_1_AST3(self):
        input = """procedure in(a:INTEGER;b,c:REAL);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'in'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_pro_param_1_AST4(self):
        input = """procedure man(a:INTEGER;b:real;c:real;d:boolean;g:boolean;f:boolean);
                var b:rEAL;c:boolean;d:boolean;g,f,h:array[3 .. 4] of real;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'man'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'g'),BoolType()),VarDecl(Id(r'f'),BoolType())],[VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'g'),ArrayType(3,4,FloatType())),VarDecl(Id(r'f'),ArrayType(3,4,FloatType())),VarDecl(Id(r'h'),ArrayType(3,4,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_pro_with_1_AST5(self):
        input = """procedure man(); 
                begin 
	                with a:real;x,c:boolean;y:INTEGER; do begin
		                with a:integer; do begin end
		                with b:real;c,t:Integer; do begin end
	                end
                end"""
        expect = str(Program([FuncDecl(Id(r'man'),[],[],[With([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'y'),IntType())],[With([VarDecl(Id(r'a'),IntType())],[]),With([VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r't'),IntType())],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_pro_if_1_AST6(self):
        input = """procedure main(); 
	            begin
	                if b > 5 then if b < 6 then b := 1; 
	                else b := 3; else b := 6;
	            end """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',Id(r'b'),IntLiteral(5)),[If(BinaryOp(r'<',Id(r'b'),IntLiteral(6)),[Assign(Id(r'b'),IntLiteral(1))],[Assign(Id(r'b'),IntLiteral(3))])],[Assign(Id(r'b'),IntLiteral(6))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_pro_for_1_AST7(self):
        input = """procedure min(); 
                begin
                    for b := 4 to 10 do begin end
                end"""
        expect = str(Program([FuncDecl(Id(r'min'),[],[],[For(Id(r'b'),IntLiteral(4),IntLiteral(10),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_fun_ret_1_AST8(self):
        input = """function mn():integeR;
                begin
                    return 9;
                end"""
        expect = str(Program([FuncDecl(Id(r'mn'),[],[],[Return(IntLiteral(9))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_pro_assign_1_AST9(self):
        input = """procedure main(); 
	            begin
	                t := t > c or else not a >= b;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r't'),BinaryOp(r'orelse',BinaryOp(r'>',Id(r't'),Id(r'c')),BinaryOp(r'>=',UnaryOp(r'not',Id(r'a')),Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_program_complex_1_AST10(self):
        input = """function foo(t:integer;x:array[5 .. 10] of integer):array [6 .. 10] of integer;
                var z:array[1 .. 9] of integer;
                begin
	                with y:integer; do 
		                if u > 0 then
			                for y := u downto a[u] do begin
				                b[y] := a[u] + x[u];
				                if y = a[x[u]] then
					                return x;
				                else
					                continue;
			                end
		                else
			        for i := 1 to n mod a[n] do begin
				        b[i] := a[i] and then x[i] or else b[i];
				        if a[x[i]] then
					        return x;
				        else
					        break;
			            end
	                    return foo(foo(x),a[x[n]]);
                    end
                    procedure main(); 
                    var i:integer;
                    begin
	                    i := getIntLn();
	                    foo(a,i);
	                    with i:integer; do
		                    for i := 3 to 10 do
			                    putIntLn(v[i]);
                    end
                var a:array[8 .. 10] of integer;"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r't'),IntType()),VarDecl(Id(r'x'),ArrayType(5,10,IntType()))],[VarDecl(Id(r'z'),ArrayType(1,9,IntType()))],[With([VarDecl(Id(r'y'),IntType())],[If(BinaryOp(r'>',Id(r'u'),IntLiteral(0)),[For(Id(r'y'),Id(r'u'),ArrayCell(Id(r'a'),Id(r'u')),False,[Assign(ArrayCell(Id(r'b'),Id(r'y')),BinaryOp(r'+',ArrayCell(Id(r'a'),Id(r'u')),ArrayCell(Id(r'x'),Id(r'u')))),If(BinaryOp(r'=',Id(r'y'),ArrayCell(Id(r'a'),ArrayCell(Id(r'x'),Id(r'u')))),[Return(Id(r'x'))],[Continue()])])],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'mod',Id(r'n'),ArrayCell(Id(r'a'),Id(r'n'))),True,[Assign(ArrayCell(Id(r'b'),Id(r'i')),BinaryOp(r'orelse',BinaryOp(r'andthen',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'x'),Id(r'i'))),ArrayCell(Id(r'b'),Id(r'i')))),If(ArrayCell(Id(r'a'),ArrayCell(Id(r'x'),Id(r'i'))),[Return(Id(r'x'))],[Break()])])])]),Return(CallExpr(Id(r'foo'),[CallExpr(Id(r'foo'),[Id(r'x')]),ArrayCell(Id(r'a'),ArrayCell(Id(r'x'),Id(r'n')))]))],ArrayType(6,10,IntType())),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'i'),IntType())],[Assign(Id(r'i'),CallExpr(Id(r'getIntLn'),[])),CallStmt(Id(r'foo'),[Id(r'a'),Id(r'i')]),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(3),IntLiteral(10),True,[CallStmt(Id(r'putIntLn'),[ArrayCell(Id(r'v'),Id(r'i'))])])])],VoidType()),VarDecl(Id(r'a'),ArrayType(8,10,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_var_1_AST11(self):
        input = """var x: iNteger;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_var_2_AST12(self):
        input = """var t: sTRing;"""
        expect = str(Program([VarDecl(Id(r't'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_var_3_AST13(self):
        input = """var a: arraY [-6 .. 3] of STrIng;"""
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(-6,3,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_var_4_AST14(self):
        input = """var a,v: arrAy [-9 .. -8] of BoolEan;"""
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(-9,-8,BoolType())),VarDecl(Id(r'v'),ArrayType(-9,-8,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_var_5_AST15(self):
        input = """var c,t: arrAy [2 .. -5] of strinG;"""
        expect = str(Program([VarDecl(Id(r'c'),ArrayType(2,-5,StringType())),VarDecl(Id(r't'),ArrayType(2,-5,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_var_6_AST16(self):
        input = """var y: inTeger;
                        w,t: stRing;"""
        expect = str(Program([VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'w'),StringType()),VarDecl(Id(r't'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_var_7_AST17(self):
        input = """var z: intEger;
                    var y,f: array [5 .. -9] of Real;"""
        expect = str(Program([VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'y'),ArrayType(5,-9,FloatType())),VarDecl(Id(r'f'),ArrayType(5,-9,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_var_8_AST18(self):
        input = """var g: integer;
                        e,k,r,w: array [1 .. 4] of strIng;"""
        expect = str(Program([VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'e'),ArrayType(1,4,StringType())),VarDecl(Id(r'k'),ArrayType(1,4,StringType())),VarDecl(Id(r'r'),ArrayType(1,4,StringType())),VarDecl(Id(r'w'),ArrayType(1,4,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_var_9_AST19(self):
        input = """var x: integer;
                        g: string;
                        i: real;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'i'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_var_10_AST20(self):
        input = """var x,y: integer;
                        g: string;
                        i: real;
                        c,d: BoolEan"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'i'),FloatType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'd'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_fun_par_var_1_AST21(self):
        input = """FUNcTION t_o(c, t: integer ; d: real):array [-1 .. 2] of Integer ;
                  var a,y: real ;
                  BEGIN
                  END"""
        expect = str(Program([FuncDecl(Id(r't_o'),[VarDecl(Id(r'c'),IntType()),VarDecl(Id(r't'),IntType()),VarDecl(Id(r'd'),FloatType())],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],ArrayType(-1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_fun_1_AST22(self):
        input = input = """function man(): inteGer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'man'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_fun_2_AST23(self):
        input = """function my_na_no(): arraY [-6 .. 7] of integer;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'my_na_no'),[],[],[],ArrayType(-6,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_fun_3_AST24(self):
        input = """function main_c(): inTeger;
                var a,b,c,d,e: IntegeR;
                BeGin
                end"""
        expect = str(Program([FuncDecl(Id(r'main_c'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'e'),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_fun_4_AST25(self):
        input = """function man_t(): arraY [-8 .. 7] of intEger;
                var heo: array [3 .. 5] of sTring;
                begin
                End"""
        expect = str(Program([FuncDecl(Id(r'man_t'),[],[VarDecl(Id(r'heo'),ArrayType(3,5,StringType()))],[],ArrayType(-8,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_fun_5_AST26(self):
        input = """function main_tr(): arraY [-3 .. 7] of iNteger;
                var ho,gy: integEr;
                    r4,t5: sTrIng;
                beGin
                eNd"""
        expect = str(Program([FuncDecl(Id(r'main_tr'),[],[VarDecl(Id(r'ho'),IntType()),VarDecl(Id(r'gy'),IntType()),VarDecl(Id(r'r4'),StringType()),VarDecl(Id(r't5'),StringType())],[],ArrayType(-3,7,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_fun_para_1_AST27(self):
        input = """function man(t: intEger;x: string): intEger;
                begin
                eNd"""
        expect = str(Program([FuncDecl(Id(r'man'),[VarDecl(Id(r't'),IntType()),VarDecl(Id(r'x'),StringType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_fun_para_2_AST28(self):
        input = """function fial(t7: boolEan;c,b: integer;r: string;d,f: array [9 .. 12] of boOLean): Array [-3 .. 6] of string;
                var a,b,d: integer;
                    g,f: booLean;
                    v: array [6 .. 2] of sTring;
                bEgin
                enD"""
        expect = str(Program([FuncDecl(Id(r'fial'),[VarDecl(Id(r't7'),BoolType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'r'),StringType()),VarDecl(Id(r'd'),ArrayType(9,12,BoolType())),VarDecl(Id(r'f'),ArrayType(9,12,BoolType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'g'),BoolType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'v'),ArrayType(6,2,StringType()))],[],ArrayType(-3,6,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_fun_para_3_AST29(self):
        input = """function falt(avs: boolEan;c,b: integer;d,f: array [3 .. 12] of boOLean): Array [-3 .. 6] of String;
                var a,b,d: integer;
                    g,f: Real;
                    v: array [9 .. 2] of sTring;
                bEgin
                enD"""
        expect = str(Program([FuncDecl(Id(r'falt'),[VarDecl(Id(r'avs'),BoolType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'd'),ArrayType(3,12,BoolType())),VarDecl(Id(r'f'),ArrayType(3,12,BoolType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r'f'),FloatType()),VarDecl(Id(r'v'),ArrayType(9,2,StringType()))],[],ArrayType(-3,6,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_pro_1_AST30(self):
        input = """procedure llo();
                var c: integeR;
                bEgin
                end"""
        expect = str(Program([FuncDecl(Id(r'llo'),[],[VarDecl(Id(r'c'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_pro_2_AST31(self):
        input = """procedure llo_f();
                var b,c: Real;
                    f,u,a: array [2 .. 9] of StrIng;
                begin
                eNd"""
        expect = str(Program([FuncDecl(Id(r'llo_f'),[],[VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'f'),ArrayType(2,9,StringType())),VarDecl(Id(r'u'),ArrayType(2,9,StringType())),VarDecl(Id(r'a'),ArrayType(2,9,StringType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_pro_3_AST32(self):
        input = """procedure pecl();
                var a,t,c: real;
                    e: array [3 .. 10] of String;
                    d: integer;
                    l: bOOLean;
                beGin
                end"""
        expect = str(Program([FuncDecl(Id(r'pecl'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'e'),ArrayType(3,10,StringType())),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'l'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_pro_para_1_AST33(self):
        input = """procedure tin(v: intEger);
                bEgin
                end"""
        expect = str(Program([FuncDecl(Id(r'tin'),[VarDecl(Id(r'v'),IntType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_pro_para_2_AST34(self):
        input = """procedure pecl(c,r: rEAl);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'pecl'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'r'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_pro_para_3_AST35(self):
        input = """procedure seiu_98(v,hg: inTeger; p,o: String);
                bEGin
                eNd"""
        expect = str(Program([FuncDecl(Id(r'seiu_98'),[VarDecl(Id(r'v'),IntType()),VarDecl(Id(r'hg'),IntType()),VarDecl(Id(r'p'),StringType()),VarDecl(Id(r'o'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_pro_para_4_AST36(self):
        input = """procedure pdecl(u: integer;c: String;d: BoolEan;f: array [2 .. 6] of BooLean;l: Real);
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'pdecl'),[VarDecl(Id(r'u'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'f'),ArrayType(2,6,BoolType())),VarDecl(Id(r'l'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_pro_para_5_AST37(self):
        input = """procedure pro_AST(t,l: String; a: integer;u: arraY[-3 .. 5] of Integer; t: arraY[6 .. 12] of Real);
                beGin
                end"""
        expect = str(Program([FuncDecl(Id(r'pro_AST'),[VarDecl(Id(r't'),StringType()),VarDecl(Id(r'l'),StringType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'u'),ArrayType(-3,5,IntType())),VarDecl(Id(r't'),ArrayType(6,12,FloatType()))],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_pro_para_6_AST38(self):
        input = """procedure prdecl(t: inTeger);
                var d: Real;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'prdecl'),[VarDecl(Id(r't'),IntType())],[VarDecl(Id(r'd'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_pro_para_7_AST39(self):
        input = """procedure prcl(g: integer;l: StrIng);
                var t: integer;
                    b: bOOlean;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'prcl'),[VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'l'),StringType())],[VarDecl(Id(r't'),IntType()),VarDecl(Id(r'b'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_pro_para_8_AST40(self):
        input = """procedure proccl(c,d: integer;y,u: String);
                var a,r: array [3 .. 6] of string;
                    r,e: bOOlean;
                begin
                end"""
        expect = str(Program([FuncDecl(Id(r'proccl'),[VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'y'),StringType()),VarDecl(Id(r'u'),StringType())],[VarDecl(Id(r'a'),ArrayType(3,6,StringType())),VarDecl(Id(r'r'),ArrayType(3,6,StringType())),VarDecl(Id(r'r'),BoolType()),VarDecl(Id(r'e'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_pro_para_9_AST41(self):
        input = """procedure pl(t: integer;y: String; u: Real; e: array [6 .. 9] of BooLean; h: BoolEan);
                var c: Real;
                    a: integer;
                    e: array [5 .. 6] of BooLean;
                    b: String; 
                    d: BoolEan;  
                beGIn
                eNd"""
        expect = str(Program([FuncDecl(Id(r'pl'),[VarDecl(Id(r't'),IntType()),VarDecl(Id(r'y'),StringType()),VarDecl(Id(r'u'),FloatType()),VarDecl(Id(r'e'),ArrayType(6,9,BoolType())),VarDecl(Id(r'h'),BoolType())],[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'e'),ArrayType(5,6,BoolType())),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'd'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_pro_assign_2_AST42(self):
        input = """procedure main(); 
	            begin
	                t := t > c;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r't'),BinaryOp(r'>',Id(r't'),Id(r'c')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_pro_assign_3_AST43(self):
        input = """procedure main(); 
	            begin
	                l := a >= b;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'l'),BinaryOp(r'>=',Id(r'a'),Id(r'b')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_pro_assign_4_AST44(self):
        input = """procedure main(); 
	            begin
	                t := t > c or else not a >= b;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r't'),BinaryOp(r'orelse',BinaryOp(r'>',Id(r't'),Id(r'c')),BinaryOp(r'>=',UnaryOp(r'not',Id(r'a')),Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_pro_assign_5_AST45(self):
        input = """procedure sat();
                begin
                    TTR := t[9] - t[99];
                end"""
        expect = str(Program([FuncDecl(Id(r'sat'),[],[],[Assign(Id(r'TTR'),BinaryOp(r'-',ArrayCell(Id(r't'),IntLiteral(9)),ArrayCell(Id(r't'),IntLiteral(99))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_pro_assign_6_AST46(self):
        input = """procedure tinh();
                begin
                    T := ((f + 2 - 6) * (3 + 5 - 4) / 49) and then 45;
                end"""
        expect = str(Program([FuncDecl(Id(r'tinh'),[],[],[Assign(Id(r'T'),BinaryOp(r'andthen',BinaryOp(r'/',BinaryOp(r'*',BinaryOp(r'-',BinaryOp(r'+',Id(r'f'),IntLiteral(2)),IntLiteral(6)),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(3),IntLiteral(5)),IntLiteral(4))),IntLiteral(49)),IntLiteral(45)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_pro_assign_7_AST47(self):
        input = """procedure txtn();
                begin
                    A := 3.1456 * (false + call_stmt(45,66,87)) or else ta[36];
                end"""
        expect = str(Program([FuncDecl(Id(r'txtn'),[],[],[Assign(Id(r'A'),BinaryOp(r'orelse',BinaryOp(r'*',FloatLiteral(3.1456),BinaryOp(r'+',BooleanLiteral(False),CallExpr(Id(r'call_stmt'),[IntLiteral(45),IntLiteral(66),IntLiteral(87)]))),ArrayCell(Id(r'ta'),IntLiteral(36))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_pro_assign_7_AST48(self):
        input = """procedure stringn();
                begin
                    A := "hello_world" + "hello_vietnam" + "hi";
                end"""
        expect = str(Program([FuncDecl(Id(r'stringn'),[],[],[Assign(Id(r'A'),BinaryOp(r'+',BinaryOp(r'+',StringLiteral(r'hello_world'),StringLiteral(r'hello_vietnam')),StringLiteral(r'hi')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_pro_assign_8_AST49(self):
        input = """procedure aray_x();
                begin
                    B:= A := C[6 + 2 * 5 - 9];
                end"""
        expect = str(Program([FuncDecl(Id(r'aray_x'),[],[],[Assign(Id(r'A'),ArrayCell(Id(r'C'),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(6),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),IntLiteral(9)))),Assign(Id(r'B'),Id(r'A'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_pro_assign_9_AST50(self):
        input = """procedure main(); 
	            begin
	                t := a:= b:= c:= halo - "ghi" mod (5 - 6) / not call(4,5 + 6,"hello" * ("h" - "6"));;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'c'),BinaryOp(r'-',Id(r'halo'),BinaryOp(r'/',BinaryOp(r'mod',StringLiteral(r'ghi'),BinaryOp(r'-',IntLiteral(5),IntLiteral(6))),UnaryOp(r'not',CallExpr(Id(r'call'),[IntLiteral(4),BinaryOp(r'+',IntLiteral(5),IntLiteral(6)),BinaryOp(r'*',StringLiteral(r'hello'),BinaryOp(r'-',StringLiteral(r'h'),StringLiteral(r'6')))]))))),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b')),Assign(Id(r't'),Id(r'a'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_exp_1_AST51(self):
        input = """procedure tll();
                begin
                    foo := 10 + cll(5)[67] - Ca[9999];
                end"""
        expect = str(Program([FuncDecl(Id(r'tll'),[],[],[Assign(Id(r'foo'),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(10),ArrayCell(CallExpr(Id(r'cll'),[IntLiteral(5)]),IntLiteral(67))),ArrayCell(Id(r'Ca'),IntLiteral(9999))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_exp_2_AST52(self):
        input = """procedure main_man();
                bEgIn
                    B := C:= cal(1,5,6,99,81)[ee[9] >= 54];
                end"""
        expect = str(Program([FuncDecl(Id(r'main_man'),[],[],[Assign(Id(r'C'),ArrayCell(CallExpr(Id(r'cal'),[IntLiteral(1),IntLiteral(5),IntLiteral(6),IntLiteral(99),IntLiteral(81)]),BinaryOp(r'>=',ArrayCell(Id(r'ee'),IntLiteral(9)),IntLiteral(54)))),Assign(Id(r'B'),Id(r'C'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_exp_3_AST53(self):
        input = """procedure mamain();
                begin
                    C:= all(9,all(6,all(9,all(8))));
                end"""
        expect = str(Program([FuncDecl(Id(r'mamain'),[],[],[Assign(Id(r'C'),CallExpr(Id(r'all'),[IntLiteral(9),CallExpr(Id(r'all'),[IntLiteral(6),CallExpr(Id(r'all'),[IntLiteral(9),CallExpr(Id(r'all'),[IntLiteral(8)])])])]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_exp_4_AST54(self):
        input = """procedure main();
                begin
                    A := hello() + hello(98);
                    B := call(6,8,9,89,69,96)[ce[3] <= 54];
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'A'),BinaryOp(r'+',CallExpr(Id(r'hello'),[]),CallExpr(Id(r'hello'),[IntLiteral(98)]))),Assign(Id(r'B'),ArrayCell(CallExpr(Id(r'call'),[IntLiteral(6),IntLiteral(8),IntLiteral(9),IntLiteral(89),IntLiteral(69),IntLiteral(96)]),BinaryOp(r'<=',ArrayCell(Id(r'ce'),IntLiteral(3)),IntLiteral(54))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_exp_5_AST55(self):
        input = """procedure mauyin();
                bEgin
                    call(9,10,36)[54] := lo := bo := 8 * 9 - 10 + 6;
                    A := call();
                eNd"""
        expect = str(Program([FuncDecl(Id(r'mauyin'),[],[],[Assign(Id(r'bo'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'*',IntLiteral(8),IntLiteral(9)),IntLiteral(10)),IntLiteral(6))),Assign(Id(r'lo'),Id(r'bo')),Assign(ArrayCell(CallExpr(Id(r'call'),[IntLiteral(9),IntLiteral(10),IntLiteral(36)]),IntLiteral(54)),Id(r'lo')),Assign(Id(r'A'),CallExpr(Id(r'call'),[]))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_stmt_if_1_AST56(self):
        input = """procedure main();
                begin
                    if 9 > 3 then d := 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',IntLiteral(9),IntLiteral(3)),[Assign(Id(r'd'),IntLiteral(4))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_stmt_if_2_AST57(self):
        input = """
        function Goo(): Real;
        begin
            if c <> 96
            then b:= 9;
        end"""
        expect = str(Program([FuncDecl(Id(r'Goo'),[],[],[If(BinaryOp(r'<>',Id(r'c'),IntLiteral(96)),[Assign(Id(r'b'),IntLiteral(9))],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_stmt_if_3_AST58(self):
        input = """procedure main();
                begin
                    if t > 3 then tcl := 2; else samsung:= 1;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',Id(r't'),IntLiteral(3)),[Assign(Id(r'tcl'),IntLiteral(2))],[Assign(Id(r'samsung'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_stmt_if_4_AST59(self):
        input = """function foo(tcl: real): inTegeR ;
                   var CA:real ;
                   BEGIN
                    if(gh>1) then gh:=1 ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'tcl'),FloatType())],[VarDecl(Id(r'CA'),FloatType())],[If(BinaryOp(r'>',Id(r'gh'),IntLiteral(1)),[Assign(Id(r'gh'),IntLiteral(1))],[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_stmt_if_5_AST60(self):
        input = """pROCEDURE tuloo(rt: real) ;
                   var der:real ;
                   BEGIN
                    if(b>1) then s:=1 ;
                    if (6<10) then beGin c:=1 ; end
                    else tuloo(s+1,2);
                   END"""
        expect = str(Program([FuncDecl(Id(r'tuloo'),[VarDecl(Id(r'rt'),FloatType())],[VarDecl(Id(r'der'),FloatType())],[If(BinaryOp(r'>',Id(r'b'),IntLiteral(1)),[Assign(Id(r's'),IntLiteral(1))],[]),If(BinaryOp(r'<',IntLiteral(6),IntLiteral(10)),[Assign(Id(r'c'),IntLiteral(1))],[CallStmt(Id(r'tuloo'),[BinaryOp(r'+',Id(r's'),IntLiteral(1)),IntLiteral(2)])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_stmt_if_6_AST61(self):
        input = """pROCEDURE foo(cclr: real) ;
                   var ty:real ;
                   BEGIN
                    if(b>6) then beGin
                        a:=1 ;
                        if(69=1) then vf:= b[1];
                        else cv:=a[1]:= 10;
                    end
                    END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'cclr'),FloatType())],[VarDecl(Id(r'ty'),FloatType())],[If(BinaryOp(r'>',Id(r'b'),IntLiteral(6)),[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'=',IntLiteral(69),IntLiteral(1)),[Assign(Id(r'vf'),ArrayCell(Id(r'b'),IntLiteral(1)))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(10)),Assign(Id(r'cv'),ArrayCell(Id(r'a'),IntLiteral(1)))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_stmt_if_7_AST62(self):
        input = """
        function footoo(): ReaL;
        begin
            if FalSe
            then
            begin
                f := 6;
                a := f;
            end
            else
            begin
                f := 96;
                a := f;
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'footoo'),[],[],[If(BooleanLiteral(False),[Assign(Id(r'f'),IntLiteral(6)),Assign(Id(r'a'),Id(r'f'))],[Assign(Id(r'f'),IntLiteral(96)),Assign(Id(r'a'),Id(r'f'))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_stmt_if_8_AST63(self):
        input = """
        function foo(): Boolean;
        begin
            If False
            then
                begin
                if false
                then aGF:=bGH;
                end
            else
            aGF:=cTH;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(False),[If(BooleanLiteral(False),[Assign(Id(r'aGF'),Id(r'bGH'))],[])],[Assign(Id(r'aGF'),Id(r'cTH'))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_assign_1_AST64(self):
        input = """
        function rooto(): integer;
        begin
            v := b := range(9,0,-6) + 9;
        end"""
        expect = str(Program([FuncDecl(Id(r'rooto'),[],[],[Assign(Id(r'b'),BinaryOp(r'+',CallExpr(Id(r'range'),[IntLiteral(9),IntLiteral(0),UnaryOp(r'-',IntLiteral(6))]),IntLiteral(9))),Assign(Id(r'v'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_assign_2_AST65(self):
        input = """
        function foo(): Integer;
        begin
            xcl := foo(969) + 9;
            a := "conga";
            b := func(1,a+1) ;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'xcl'),BinaryOp(r'+',CallExpr(Id(r'foo'),[IntLiteral(969)]),IntLiteral(9))),Assign(Id(r'a'),StringLiteral(r'conga')),Assign(Id(r'b'),CallExpr(Id(r'func'),[IntLiteral(1),BinaryOp(r'+',Id(r'a'),IntLiteral(1))]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_assign_3_AST66(self):
        input = """
        function foo(): integer;
        begin
            ade := bck[58] := foo()[96] := xtl := 8+9;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'xtl'),BinaryOp(r'+',IntLiteral(8),IntLiteral(9))),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(96)),Id(r'xtl')),Assign(ArrayCell(Id(r'bck'),IntLiteral(58)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(96))),Assign(Id(r'ade'),ArrayCell(Id(r'bck'),IntLiteral(58)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_compound_1_AST67(self):
        input = """function foo(tcl: rEAl): inTEger;
                   BEGIN
                    while (9=6) do begin eND
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'tcl'),FloatType())],[],[While(BinaryOp(r'=',IntLiteral(9),IntLiteral(6)),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test_compound_2_AST68(self):
        input = """
        function foop(): inTEger;
        begin
            xer := 8;
            begin
                xrt:=25;
                xrt:=32;
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'foop'),[],[],[Assign(Id(r'xer'),IntLiteral(8)),Assign(Id(r'xrt'),IntLiteral(25)),Assign(Id(r'xrt'),IntLiteral(32))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_for_1_AST69(self):
        input = """
        function foo(): Boolean;
        begin
            for ctf := 9 TO 12 DO a:=ctf;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'ctf'),IntLiteral(9),IntLiteral(12),True,[Assign(Id(r'a'),Id(r'ctf'))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    
    def test_for_2_AST70(self):
        input = """
        function foooo(): Real;
        begin
            for xlc := 12 downTO 9 DO
                begin
                    c := xlc + 9;
                    f := xlc - 6;
                end
        end"""
        expect = str(Program([FuncDecl(Id(r'foooo'),[],[],[For(Id(r'xlc'),IntLiteral(12),IntLiteral(9),False,[Assign(Id(r'c'),BinaryOp(r'+',Id(r'xlc'),IntLiteral(9))),Assign(Id(r'f'),BinaryOp(r'-',Id(r'xlc'),IntLiteral(6)))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_for_3_AST71(self):
        input = """
        function foo_69(): integer;
        begin
            xlc := 9;
            for i := 1 TO 10 DO
                xlc := xlc + i + 3;
        end"""
        expect = str(Program([FuncDecl(Id(r'foo_69'),[],[],[Assign(Id(r'xlc'),IntLiteral(9)),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'xlc'),BinaryOp(r'+',BinaryOp(r'+',Id(r'xlc'),Id(r'i')),IntLiteral(3)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_for_4_AST72(self):
        input = """procedure maintainc(); 
                begin
                    for ast:=9 to 12 do ast:=10;
                end"""
        expect = str(Program([FuncDecl(Id(r'maintainc'),[],[],[For(Id(r'ast'),IntLiteral(9),IntLiteral(12),True,[Assign(Id(r'ast'),IntLiteral(10))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_for_5_AST73(self):
        input = """pROCEDURE fre(ctx: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>5 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=fre(10);
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'fre'),[VarDecl(Id(r'ctx'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),IntLiteral(10)),True,[While(BinaryOp(r'>',Id(r'i'),IntLiteral(5)),[For(Id(r'i'),BinaryOp(r'+',Id(r'm'),IntLiteral(1)),IntLiteral(10),False,[While(BinaryOp(r'>',Id(r'j'),IntLiteral(1)),[Assign(Id(r'x'),CallExpr(Id(r'fre'),[IntLiteral(10)]))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_while_1_AST74(self):
        input = """
        function rtoo(): integer;
        begin
            while tyu DO tyu:= true;
        end"""
        expect = str(Program([FuncDecl(Id(r'rtoo'),[],[],[While(Id(r'tyu'),[Assign(Id(r'tyu'),BooleanLiteral(True))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_while_2_AST75(self):
        input = """
        function rotoo(): Real;
        begin
            for rt := 9 to 12 do
                while i = 1 do
                    i := 10;
        end"""
        expect = str(Program([FuncDecl(Id(r'rotoo'),[],[],[For(Id(r'rt'),IntLiteral(9),IntLiteral(12),True,[While(BinaryOp(r'=',Id(r'i'),IntLiteral(1)),[Assign(Id(r'i'),IntLiteral(10))])])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_while_3_AST76(self):
        input = """pROCEDURE foo(ctv: real) ;
                   BEGIN
                    whILe(af<>1) do beGin
                        while(1) do x:=9;
                        if(a=9) then begin end
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'ctv'),FloatType())],[],[While(BinaryOp(r'<>',Id(r'af'),IntLiteral(1)),[While(IntLiteral(1),[Assign(Id(r'x'),IntLiteral(9))]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(9)),[],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_while_4_AST77(self):
        input = """
        function foo(): Real;
        begin
            while CTX DO
            begin
                CTX:= false;
                zty:= yetr;
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(Id(r'CTX'),[Assign(Id(r'CTX'),BooleanLiteral(False)),Assign(Id(r'zty'),Id(r'yetr'))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_break_1_AST78(self):
        input = """
        function f9oo(): integer;
        begin
            xrt := 89;
            breaK;
        end"""
        expect = str(Program([FuncDecl(Id(r'f9oo'),[],[],[Assign(Id(r'xrt'),IntLiteral(89)),Break()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_break_2_AST79(self):
        input = """
        function foo(): integer;
        begin
            while trx >= acs DO
            Begin
                trxx := 912;
                breaK;
            End
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[While(BinaryOp(r'>=',Id(r'trx'),Id(r'acs')),[Assign(Id(r'trxx'),IntLiteral(912)),Break()])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_break_3_AST80(self):
        input = """pROCEDURE foo(asr: real);
                   BEGIN
                    FOR ti:=9 to m+12 do beGin
                        brEaK;
                    end
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'asr'),FloatType())],[],[For(Id(r'ti'),IntLiteral(9),BinaryOp(r'+',Id(r'm'),IntLiteral(12)),True,[Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_continue_1_AST81(self):
        input = """procedure foomain();
                begin
                    continue;
                end"""
        expect = str(Program([FuncDecl(Id(r'foomain'),[],[],[Continue()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_continue_2_AST82(self):
        input = """pROCEDURE mainfoo(crt: real);
                   BEGIN
                    while (true) do continuE ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'mainfoo'),[VarDecl(Id(r'crt'),FloatType())],[],[While(BooleanLiteral(True),[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_return_1_AST83(self):
        input = """procedure main();
                begin
                    return itme >= 9 * 6;
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Return(BinaryOp(r'>=',Id(r'itme'),BinaryOp(r'*',IntLiteral(9),IntLiteral(6))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_return_2_AST84(self):
        input = """procedure main(); 
	            begin
	                t := t > c or else not a >= b;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r't'),BinaryOp(r'orelse',BinaryOp(r'>',Id(r't'),Id(r'c')),BinaryOp(r'>=',UnaryOp(r'not',Id(r'a')),Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_with_1_AST85(self):
        input = """
        function mafoo(): Real;
        begin
            with dtv: iNteger; do dtv := 63;
        end"""
        expect = str(Program([FuncDecl(Id(r'mafoo'),[],[],[With([VarDecl(Id(r'dtv'),IntType())],[Assign(Id(r'dtv'),IntLiteral(63))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_with_2_AST86(self):
        input = """
        function trfoo(): integer;
        begin
            with s,m:integer; c: array [8 .. 12] of real; do
                begin
                    s := 9;
                    d := c[a] + m;
                end
        end"""
        expect = str(Program([FuncDecl(Id(r'trfoo'),[],[],[With([VarDecl(Id(r's'),IntType()),VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'c'),ArrayType(8,12,FloatType()))],[Assign(Id(r's'),IntLiteral(9)),Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'm')))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_with_3_AST87(self):
        input = """procedurE foo123 (b : real) ;
                var atm : array [2 .. 3] of integer;
                    dft: boolean;
                    ber: string;
                    cer: real;
                begin
                    while(atm=9) do
                        with a,b,c:integer;b: array [1 .. 3] of StRing; do 
                            while(a=6) do
                                with a,b,c:integer;b: array [1 .. 3] of StRing; do
                                    e:=96;
                End"""
        expect = str(Program([FuncDecl(Id(r'foo123'),[VarDecl(Id(r'b'),FloatType())],[VarDecl(Id(r'atm'),ArrayType(2,3,IntType())),VarDecl(Id(r'dft'),BoolType()),VarDecl(Id(r'ber'),StringType()),VarDecl(Id(r'cer'),FloatType())],[While(BinaryOp(r'=',Id(r'atm'),IntLiteral(9)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(6)),[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,StringType()))],[Assign(Id(r'e'),IntLiteral(96))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_call_1_AST88(self):
        input = """
        function main(): Real;
        begin
            goo();
            foo();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'goo'),[]),CallStmt(Id(r'foo'),[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_call_2_AST89(self):
        input = """function mainten(rec: real): integer;
                   BEGIN
                    foo(3,tam+9,tam<>1,tam[2]);
                    return 12;
                   END"""
        expect = str(Program([FuncDecl(Id(r'mainten'),[VarDecl(Id(r'rec'),FloatType())],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp(r'+',Id(r'tam'),IntLiteral(9)),BinaryOp(r'<>',Id(r'tam'),IntLiteral(1)),ArrayCell(Id(r'tam'),IntLiteral(2))]),Return(IntLiteral(12))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_call_3_AST90(self):
        input = """function maifoo(ctc: real): integer;
                   BEGIN
                    foo1(9,foo(foo1(foo2(12,a+1))));
                    return func2(a(1,2));
                   END"""
        expect = str(Program([FuncDecl(Id(r'maifoo'),[VarDecl(Id(r'ctc'),FloatType())],[],[CallStmt(Id(r'foo1'),[IntLiteral(9),CallExpr(Id(r'foo'),[CallExpr(Id(r'foo1'),[CallExpr(Id(r'foo2'),[IntLiteral(12),BinaryOp(r'+',Id(r'a'),IntLiteral(1))])])])]),Return(CallExpr(Id(r'func2'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_complex_1_AST91(self):
        input = """
                procedure maintain() ;
                beGin
                 cv[bt[8]] := 10;
                 foo();
                 return;
                eND
                """
        expect = str(Program([FuncDecl(Id(r'maintain'),[],[],[Assign(ArrayCell(Id(r'cv'),ArrayCell(Id(r'bt'),IntLiteral(8))),IntLiteral(10)),CallStmt(Id(r'foo'),[]),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_complex_2_AST92(self):
        input = """
                procedure main() ;
                var a: array[0 .. m-1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n - 2 do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then beGin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),ArrayType(0,-1,IntType())),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),IntLiteral(0),BinaryOp(r'-',Id(r'n'),IntLiteral(2)),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp(r'>',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'temp'))],[])])]),CallStmt(Id(r'print'),[Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_complex_3_AST93(self):
        input = """
                Function Tong_So_Chia_Het_Cho3(ART:array[0 .. 10] of inTeger ; N:Integer):Integer;
                Var S,P :Integer;
                Begin
                	S:=0;
                	For P:=0 to N do
                	If(ART[i] mod 3=0) then
                	S := S+ART[i];
                	return S;
                End
                """
        expect = str(Program([FuncDecl(Id(r'Tong_So_Chia_Het_Cho3'),[VarDecl(Id(r'ART'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'S'),IntType()),VarDecl(Id(r'P'),IntType())],[Assign(Id(r'S'),IntLiteral(0)),For(Id(r'P'),IntLiteral(0),Id(r'N'),True,[If(BinaryOp(r'=',BinaryOp(r'mod',ArrayCell(Id(r'ART'),Id(r'i')),IntLiteral(3)),IntLiteral(0)),[Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),ArrayCell(Id(r'ART'),Id(r'i'))))],[])]),Return(Id(r'S'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_complex_4_AST94(self):
        input = """procedure main(); 
	            begin
	                t := t > c or else not a >= b;
	            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r't'),BinaryOp(r'orelse',BinaryOp(r'>',Id(r't'),Id(r'c')),BinaryOp(r'>=',UnaryOp(r'not',Id(r'a')),Id(r'b'))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_complex_5_AST95(self):
        input = """function main_c(): sTring;
                begin
                    return bts + 4;
                end
                procedure main_b();
                begin
                    for tsm:= we * 9 / 3 to f + 12 * 6 mod 3 do
                        if (89 = 3) then
                            return tsm / 2 and dcv + 3 > a or else 4;
                end"""
        expect = str(Program([FuncDecl(Id(r'main_c'),[],[],[Return(BinaryOp(r'+',Id(r'bts'),IntLiteral(4)))],StringType()),FuncDecl(Id(r'main_b'),[],[],[For(Id(r'tsm'),BinaryOp(r'/',BinaryOp(r'*',Id(r'we'),IntLiteral(9)),IntLiteral(3)),BinaryOp(r'+',Id(r'f'),BinaryOp(r'mod',BinaryOp(r'*',IntLiteral(12),IntLiteral(6)),IntLiteral(3))),True,[If(BinaryOp(r'=',IntLiteral(89),IntLiteral(3)),[Return(BinaryOp(r'orelse',BinaryOp(r'>',BinaryOp(r'+',BinaryOp(r'and',BinaryOp(r'/',Id(r'tsm'),IntLiteral(2)),Id(r'dcv')),IntLiteral(3)),Id(r'a')),IntLiteral(4)))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_complex_6_AST96(self):
        input = """var nel : integer;
                function power_5(ner:integer): integer;
                var kfr : integer;
                begin
                    kfr := 0;
                    while (ner mod 5 = 0) do
                    begin
                        kfr := succ(kfr);
                        ner := ner div 5;
                    end
                    power_5 := kfr;
                end"""
        expect = str(Program([VarDecl(Id(r'nel'),IntType()),FuncDecl(Id(r'power_5'),[VarDecl(Id(r'ner'),IntType())],[VarDecl(Id(r'kfr'),IntType())],[Assign(Id(r'kfr'),IntLiteral(0)),While(BinaryOp(r'=',BinaryOp(r'mod',Id(r'ner'),IntLiteral(5)),IntLiteral(0)),[Assign(Id(r'kfr'),CallExpr(Id(r'succ'),[Id(r'kfr')])),Assign(Id(r'ner'),BinaryOp(r'div',Id(r'ner'),IntLiteral(5)))]),Assign(Id(r'power_5'),Id(r'kfr'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_complex_7_AST97(self):
        input ="""procedure a();
                begin
                atr:= 5.2;
                ber:= 3.1e1;
                cty:= 9.e-2;
                dfg:= 3.2e1;
                rf:= .5e23;
                yug:= -1e-7;
                uib:= -3.6e1;
                gre:= -3.4e-1;
            end"""
        expect = str(Program([FuncDecl(Id(r'a'),[],[],[Assign(Id(r'atr'),FloatLiteral(5.2)),Assign(Id(r'ber'),FloatLiteral(31.0)),Assign(Id(r'cty'),FloatLiteral(0.09)),Assign(Id(r'dfg'),FloatLiteral(32.0)),Assign(Id(r'rf'),FloatLiteral(5e+22)),Assign(Id(r'yug'),UnaryOp(r'-',FloatLiteral(1e-07))),Assign(Id(r'uib'),UnaryOp(r'-',FloatLiteral(36.0))),Assign(Id(r'gre'),UnaryOp(r'-',FloatLiteral(0.34)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test_complex_8_AST98(self):
        input = """procedure main();
                begin
                    if a then
                        if b then
                            if c then
                                f();
                            else g();
                        else c();
                end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(Id(r'a'),[If(Id(r'b'),[If(Id(r'c'),[CallStmt(Id(r'f'),[])],[CallStmt(Id(r'g'),[])])],[CallStmt(Id(r'c'),[])])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_complex_9_AST99(self):
        input = """
                Function UCLN(a,b:integer):iNTeger;
                Begin
                 If(a=b) then RETURN b ;
                 else
                  If (a>b) then return UCLN(a-b,b);
                  else return UCLN(a,b-a);
                End
                """
        expect = str(Program([FuncDecl(Id(r'UCLN'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Return(Id(r'b'))],[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Return(CallExpr(Id(r'UCLN'),[BinaryOp(r'-',Id(r'a'),Id(r'b')),Id(r'b')]))],[Return(CallExpr(Id(r'UCLN'),[Id(r'a'),BinaryOp(r'-',Id(r'b'),Id(r'a'))]))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_complex_10_AST100(self):
        input = """procedure mainain(); 
                begin
                    if art then fel[art] := 96; else begin
                        for art:= 9  downto 1 do begin
                            if art> 36 then continue; else break;
                        end
                    end
                end"""
        expect = str(Program([FuncDecl(Id(r'mainain'),[],[],[If(Id(r'art'),[Assign(ArrayCell(Id(r'fel'),Id(r'art')),IntLiteral(96))],[For(Id(r'art'),IntLiteral(9),IntLiteral(1),False,[If(BinaryOp(r'>',Id(r'art'),IntLiteral(36)),[Continue()],[Break()])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,400))