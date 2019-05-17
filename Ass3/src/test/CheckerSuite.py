import unittest
from TestUtils import TestChecker
from AST import *
#####################################test_case_mau##################################################
# def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin foo();end"""
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         putIntLn();
    #     end"""
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],[],[
    #         CallStmt(Id("foo"),[])])])
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],[],[
    #                 CallStmt(Id("putIntLn"),[])])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,403))
#############################################################################################################
class CheckerSuite(unittest.TestCase):
    def test_redeclare_1(self):
        input = """Procedure main(); begin end procedure foo(); begin end procedure pUtIntLn(); begin end"""
        expect = "Redeclared Procedure: pUtIntLn"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare_2(self):
        input = """Procedure main(); begin end procedure foo(a: integer;a: integer ); begin end"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclare_3(self):
        input = """Procedure main(); begin end procedure foo(a: integer;b: integer); var a: integer; begin end"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403)) 

    def test_redeclare_4(self):
        input = """Procedure main(); begin end procedure foo(c: integer;b: integer); var a: integer; a:Real; begin end"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404)) 

    def test_redeclare_5(self):
        input = """Procedure mAiN(); begin end Var a: integer; b,a: Real;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405)) 

    def test_undeclared_6(self):
        input = """Procedure mAiN(); begin end procedure foo(a: integer;b: integer); begin a:= b:= too(1); end Var a: integer; b: Real;"""
        expect = "Undeclared Function: too"
        self.assertTrue(TestChecker.test(input,expect,406)) 

    def test_undeclared_7(self):
        input = """Procedure mAiN(); begin end procedure foo(a: integer;c: integer); begin a:= b:= foo(1,3); end Var a: integer; c: Real;"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,407)) 
    
    def test_undeclared_8(self):
        input = """procedure main(); 
	            begin
	                if b > 5 then if b < 6 then b := 1; 
	                else b := 3; else b := 6;
	            end"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,408)) 
    
    def test_undeclared_9(self):
        input = """procedure main(); 
	            begin
	                foo();
	            end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,409)) 

    def test_undeclared_10(self):
        input = """procedure main(); 
                var a: integer;
	            begin
	                a := foo();
	            end"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclare_11(self):
        input = """var se,tr,as : integer ;
                var as: integer;
                procedure main(); 
                begin
	                return;
                end"""
        expect = "Redeclared Variable: as"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclare_12(self):
        input = """var  tes,b,ced:integer;
                var der,b:integer;
                procedure main(); 
                begin
	                return;
                end"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclare_13(self):
        input = """var art, big:integer;
                var d: real;
                procedure mr(); var n:integer; begin end 
                procedure nt(); var c:integer; begin end
                function  cy(a,b:integer):real; begin return 10; end
                procedure d(); begin end
                procedure main(); begin 
	                mr();nt();cy(1,2);d();
	                return ;
                end"""
        expect = "Redeclared Procedure: d"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclare_14(self):
        input = """var c: integer;
                var  def:real;
                var  ef:boolean;
                function foo(ber, ar : integer;  miy:array[1 .. 3] of integer):integer; 
                begin 
	                with a: array[1 .. 10] of integer; do 
                        begin 
	                    end
	                return 0;
                end
                function foo1(brt, c:integer; miy:array [1 .. 3] of integer):integer; 
                var c:array[1 .. 5] of integer;
                begin 
	                return 0;
                end
                procedure main(); var a:array[1 .. 3] of integer;
                begin  
                    a[9] := foo(5,foo1(1,2,a),a);
                return ;
                end"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_15(self):
        input = """var  d:real;
                var  e:boolean;
                procedure main(); 
                begin 
	                for temp := 1 to 10 do 
                    begin 
	                end
                end"""
        expect = "Undeclared Identifier: temp"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_16(self):
        input = """var art:integer;
                procedure funcA();
                var buy:integer; 
                begin 
	                art := 7;
	                buy := art;
                end
                function sum(b:integer):integer; 
                var der:integer;
                begin 
	                der := 7;
	                return art + b + der;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
	                m[9] := sum(6);
	                funcA();
	                art := 9 + n[1];
	                return ;
                end"""
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_17(self):
        input = """var a:integer;
                function foo(a, b:integer):integer; 
                begin 
	                if (a > b) then a := 1 + b;
	                else a := b + 2;
	                return a;
                end
                function foo1(a:integer):integer;
                var b, c, deg:integer;
                begin 
	                b := 2;
	                c := 3;
	                if (a > b) then deg := a + c;
	                else deg := b + foo2(1);
	                return deg;
                end
                var b:integer;
                function foo2(art:integer):integer;
                begin 
	                while (art > 5) do art := art + 1;
	                    return art;
                end
                procedure main(); 
                begin 
	                a := foo(foo1(1),foo2(2));
	                funy98(4);
	                return ;
                end"""
        expect = "Undeclared Procedure: funy98"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_18(self): #test 15
        input = """function foo():integer;
                var a:integer;
                begin  
	                a := 4;
	                if (a = 10) then begin 
		                return 1; 
	                end
	                return 10;
                end

                procedure main(); 
                var art:integer;
                begin 
	                art := 0;
	                if (foo() > 1) then 
                    begin 
		                if(foo9() <= 100) then
			                return ; 
		                else
			                return ;  
	                end 
	                else 
                    begin 
		                art := 96;
		                return ;
	                end
                end"""
        expect = "Undeclared Function: foo9"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_TypeMismatchInStatement_19(self):
        input = """procedure main();
                var  art, ier, jrt:integer; 
                begin 
	                for ier := 1 to 10 do 
                    begin 
		                jrt := 9;
	                end	
	                for art := 0 to  5 = 3 do 
                    begin 
		                jrt := 6;
	                end
	                return ;
                end"""
        expect = "Type Mismatch In Statement: For(Id(art)IntLiteral(0),BinaryOp(=,IntLiteral(5),IntLiteral(3)),True,[AssignStmt(Id(jrt),IntLiteral(6))])"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_TypeMismatchInStatement_20(self):
        input = """function fo():integer; begin  return 1; end
                function fo1():integer; begin  return 9.5; end
                procedure main(); 
                begin 
                    return ;
                end"""
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(9.5)))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_TypeMismatchInStatement_21(self):
        input = """function foo():boolean; begin  return 9 > 1; end
                function oo1(a:integer):boolean; begin  return a = 1; end
                function oo2(art:integer):boolean; begin  return art; end
                procedure main(); 
                begin 
                    return ;
                end"""
        expect = "Type Mismatch In Statement: Return(Some(Id(art)))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_TypeMismatchInExpression_22(self):
        input = """var art, bit, cer:integer;
                var d:boolean;
                var ert:real;
                var m: array [1 .. 100] of integer;
                function foo():integer; 
                begin  
                    return 0; 
                end
                procedure main(); 
                begin 
                    bit := foo();
                    d := true;
                    art := m[0] + 1;
                    cer := m[d] + 1;
                    return ;
                end"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(m),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_TypeMismatchInStatement_23(self):
        input = """var a:integer;
                var t:real;
                var C:array[1 .. 10] of integer;
                procedure main(); 
                begin 
                    t := C[1] + -1;
                    t := t * (1.0 + 1);
                    t := not (C[1] = 1);
                    return ;
                end"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),UnaryOp(not,BinaryOp(=,ArrayCell(Id(C),IntLiteral(1)),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_BreakNotInLoop_24(self):
        input = """var a, b, c:integer;
                procedure foo(); 
                begin 
                    while (a < 100) do
                     begin
                        a := a + 1;
                        break;
                    end
                    return ;
                end
                procedure main(); 
                begin 
                    while (a < 100) do 
                    begin
                        a := a + 1;
                        break;
                    end
                        foo();
                    if(a = 100) then break;
                    return ;
                end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_no_entry_point_25(self):
        input = """var  d:real;
                var  e:boolean;
                function main(b, a : integer;  m:array[1 .. 3] of integer): integer; 
                begin 
	                for a := 1 to 10 do 
                    begin 
	                end
	                return 0;
                end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_no_entry_point_26(self):
        input = """var  d:real;
                var  e:boolean;
                procedure to_(b, a : integer;  m:array[1 .. 3] of integer); 
                begin 
	                for a := 1 to 10 do 
                    begin 
	                end
                end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_no_entry_point_27(self):
        input = """var  d:real;
                var  e:boolean;
                var mAIn: integer;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_28(self):
        input = """var  d:real;
                var  e:boolean;
                procedure main(); 
                begin 
	                for main := 1 to 10 do 
                    begin 
	                end
                end"""
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_29(self):
        input = """var  d:real;
                var  e:boolean;
                procedure main(); 
                begin 
	                for a := 1 to 10 do 
                    begin 
	                end
                end
                procedure foo(b, a : integer);
                begin
                    b := a;
                end"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_30(self):
        input = """var  d:real;
                var  e:boolean;
                procedure main(); 
                begin 
	                if d = 1 then
                    begin 
	                end
                end

                procedure foo(b, a : integer);
                begin
                    b2();
                end

                function b2():integer;
                begin
                    return 10;
                end"""
        expect = "Undeclared Procedure: b2"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_redeclare_31(self):
        input = """Procedure main(); 
                begin 
                end 
                procedure foo(c: integer;b: integer); 
                var a: integer; d:Real; 
                begin 
                    with temp , temp : integer; do
                        begin
                            return;
                        end
                end"""
        expect = "Redeclared Variable: temp"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMismatchInStatement_32(self):
        input = """var  d:real;
                var  e:boolean;
                var a: integer;
                procedure main(); 
                begin 
	                for a := 1 to 10 do 
                    begin 
	                end
                end
                Function foo(b, a : integer): integer;
                begin
                    for a := 1 to 10 do 
                        begin 
	                    end
                    return 1;
                end
                procedure b2();
                begin
                    e := 12;
                end"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(e),IntLiteral(12))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_no_entry_point_33(self):
        input = """var  d:real;
                var  e:boolean;
                procedure main(ast: integer); 
                begin 
	                if d = 1 then
                    begin 
	                end
                end

                procedure foo(b, a : integer);
                begin
                    a := b2();
                end

                function b2():integer;
                begin
                    return 10;
                end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_no_entry_point_34(self):
        input = """procedure main(main:integer);
                begin
                    main:=main+1;
                end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_no_entry_point_35(self):
        input = """
            procedure foo23(art: array[-9 .. 2] of integer;biy:integer);
            begin
                return;
            end
            procedure main(atr:integer);
            begin 
            end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_no_entry_point_36(self):
        input = """
            var xit: array [-6 .. 2] of integer;var ctx:real;var d:integer;
            function main12(): integer;
            begin 
                return 1; 
            end
            function main(): real ;var ety:integer ; 
            begin
                return 1;
            end
		"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_no_entry_point_37(self):
        input = """function foo():real; 
            begin
		        if (9.1>6.9) then
			        begin
			            return 8.0;
			        end
			    return 10.0;
		    end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_no_entry_point_38(self):
        input = """"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_no_entry_point_39(self):
        input = """
            function foo2():real;
            var ier:integer;
            begin
                with i:integer; do return 10; // Ok
                
            end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_no_entry_point_40(self):
        input = """
            function too():real;
            var ier:integer;
            begin
                for ier:=1 to ier do 
                    begin
                        for ier:=1 to ier do
                            break;
                    end
                    return 0;
            end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_no_entry_point_41(self):
        input = """
            procedure main(i:integer);
            begin
                with ier:real; do ier:=foo3();
            end
            function foo3():real;
            var itr:integer;
            begin
                for itr:=1 to itr do 
                    begin
                        for itr:=1 to itr do
                            break;
                        break;
                    end
                    return 0;
            end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_BreakNotInLoop_42(self):
        input = """procedure main();
            begin
                while (8>1) do begin end
                break;
            end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,442))


    def test_BreakNotInLoop_43(self):
        input = """procedure main();
		begin
			while (9>8) do begin
				if 6>7 then
				begin
					with art:integer; do begin
						continue;
					end
				end
			end
			break;
		end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_BreakNotInLoop_44(self):
        input = """PROCEDURE Main( ); 
            var ctc:integer;     	
            begin   
                while false do
                begin
                    for ctc:=1 to 9 do break;
                    continue; 
                end
                break;
            end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_BreakNotInLoop_45(self):
        input ="""PROCEDURE Main();  
                var art:integer;     	
                begin   
                    if true then break;   
                end
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_BreakNotInLoop_46(self):
        input = """
            procedure main();
            var art:array[ 1 .. 99 ] of integer;
            begin
                with ity:real; do ity:=foo1();
            end

            function foo1():real;
            var iy:integer;
            begin
                for iy:=1 to 10 do break; break;
                
            end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_BreakNotInLoop_47(self):
        input = """procedure main();
            begin
                with i:real; do i:=foo();
            end
            function foo():real;
            var i:integer;
            begin
                for i:=1 to i do 
                    for i:=1 to i do
                        break;
                break;
                return 0;
            end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,47))

    def test_BreakNotInLoop_48(self):
        input = """procedure main();
            begin
                with i:integer; do i:=-----------------------------i; // Trying to catch ast error
                break;
            end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_BreakNotInLoop_49(self):
        input = """procedure main();
            begin
                with i:boolean; do i:=not not not not not not not not not not i; // Trying to catch ast error
                break;
            end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_BreakNotInLoop_50(self):
        input = """procedure main();
            begin
                putLn(); // Ok
                PUTINTLN(10);// Ok
                break;// Error
            end"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_Type_Mismatch_In_Statement_Return_51(self):
        input = """
        procedure main();
        var
            i: integer;
            r: real;
            s: string;
            b: boolean;
        begin
            for i:=1 to 10 do return 1;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_diff_numofparam_stmt_52(self):
        """More complex program"""
        input = """procedure main(); 
        begin
            putIntLn();
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_undeclared_function_use_ast_53(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"), [], [], [
            CallStmt(Id("foo"), [])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_diff_numofparam_expr_use_ast_54(self):
        """More complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], [], [CallStmt(Id("putIntLn"), [])])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_undeclared_function_55(self):
        input = """
        function foo():integer;
        begin
            return 1;
        end
        procedure main();
        begin
            foo();
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_return_stmt2_56(self):
        input = """
        var a: integer;
        procedure main();
        begin
            a := foo();
        end
        function foo(): integer;
        var a: boolean;
        begin
            if (1>0) then
            return;
            else
            return 1;
        end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_global1_57(self):
        input = """
        function f(i:integer ; j:real):integer;
        var a:integer;
            b:boolean;
            c:string;
            d:integer;
        begin
            with a,b:real; c:array [1 .. 2] of real; do
                begin
                    a := c[d] +b;
                    putIntLn(a);
                    return a;
                end
        end
        procedure main();
        var i: integer;
        begin
            i := f(1,2.3);
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_global2_58(self):
        input = """
        procedure Main32( c: real);
            var Main32: real;      
            begin 
                    if true then Main32(1);   
            end
        procedure Main();
        begin 
        end
        """
        expect = "Undeclared Procedure: Main32"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_function_not_return_59(self):
        input = """
        function foo():integer;
        var a:integer;
        begin
            while 1>0 do
            begin
                return 1;
            end
            a:=a+1;
        end
        procedure Main();
        var a:integer;
        begin 
            a:= foo();
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_return_array_60(self):
        input = """
        procedure main();
        begin
            return;
        end
        function foo(): array [1 .. 10] of integer;
        var a: array [1 .. 9] of integer;
        begin
            return a;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_redeclare_function_61(self):
        input = """
        function foo(): integer;
        var foo: real;
        begin
            foo := foo();
            return 1;
        end
        procedure main();
        var i:integer;
        begin
            i:=foo();
            return;
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 461))
    

    def test_for_stmt_62(self):
        input = """
        var a: integer;
        procedure main();
        begin
                foo(5);
        end
        procedure foo(b: integer);
        var c: integer;
        begin
                for a := 1.1 to 10 do foo(1);
                for b := 1 to 10 do foo(1);
                for c := 1 to 10 do foo(1);
        end
        """
        expect = "Type Mismatch In Statement: For(Id(a)FloatLiteral(1.1),IntLiteral(10),True,[CallStmt(Id(foo),[IntLiteral(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_redeclare_function1_63(self):
        input = """
        function foo(): integer;
        var i: real;
        begin
            return 1;
        end
        function foo(): real;
        var i: real;
        begin
            return 1;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_14(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		begin
			while (2>1) do begin
				if 2>1 then begin 
					if 2>1 then break;
					else 
					begin
						while 2>1 do begin 
							break;
						end
						continue;
					end
				end
				else return 2;
			end
		end"""
		expect = "Type Mismatch In Statement: Return(Some(IntLiteral(2)))"
		self.assertTrue(TestChecker.test(input,expect,412))
	def test_15(self):
		"""Simple program: int main() {} """
		input = """procedure main(a:integer;i:boolean);
		begin
			a:=i;
		end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(i))"
		self.assertTrue(TestChecker.test(input,expect,413))
	def test_16(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		var a:integer;
		i:integer;
		begin
			e:=c+1;
		end"""
		expect = "Undeclared Identifier: e"
		self.assertTrue(TestChecker.test(input,expect,414))
	def test_17(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		var a:integer;
		i:integer;
		begin
			i:=True;
		end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(i),BooleanLiteral(True))"
		self.assertTrue(TestChecker.test(input,expect,418))
	def test_18(self):
		"""Simple program: int main() {} """
		input = """procedure main();
					var a:integer;b:integer;c:real;
					begin
						for a := a*b*b*a*a to 25 do
						begin
							while(a <= 54) do
							begin
								if(a*b > 0) then break;
								
								for a := a*b*b to 25 do return 2.2;
								
							end
							break;
						end
					end
					procedure main();
					begin
					
					end
					"""
		expect = "Redeclared Procedure: main"
		self.assertTrue(TestChecker.test(input,expect,415))
	def test_19(self):
		"""Simple program: int main() {} """
		input = """
		function foo(a:array [1 .. 2] of real):array[1 .. 2] of integer;
		var b:array [1 .. 2] of real;
		begin
		return b;
		end
		procedure main();
					var a:array[1 .. 2] of real;
					begin
						foo(a)[1]:=2;
					end
					"""
		expect = "Type Mismatch In Statement: Return(Some(Id(b)))"
		self.assertTrue(TestChecker.test(input,expect,419))
	def test_20(self):
		"""Simple program: int main() {} """
		input = """
		procedure main();
					var a:array[1 .. 2] of real;
					begin
						s:=s+1;
						a[s]:=True;
					end
					var s:integer;
					"""
		expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),Id(s)),BooleanLiteral(True))"
		self.assertTrue(TestChecker.test(input,expect,420))
	def test_21(self):
		"""Simple program: int main() {} """
		input = """
		function foo(i:integer):real;
		begin
			for i:=1 to 2 do
			begin
				return i;
			end
			return i;
		end
		procedure main();
					var i:integer;
					begin
						i:=foo(i);
					end
					"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(i),CallExpr(Id(foo),[Id(i)]))"
		self.assertTrue(TestChecker.test(input,expect,421))
	def test_22(self):
		"""Simple program: int main() {} """
		input = """
		function foo(i:integer):real;
		begin
			for i:=1 to 2 do
			begin
				return i;
			end
			return i;
		end
		procedure main();
					var i:integer;
					begin
						foo(i);
					end
					"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,422))
	def test_23(self):
		"""Simple program: int main() {} """
		input = """
		function foo(i:integer):real;
		begin
			for i:=1 to 2 do
			begin
				return i;
			end
			return i;
		end
		procedure main();
					var i:integer;
					begin
						i:=foo(i);
						while(2>1)do
							return;
					end
					"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(i),CallExpr(Id(foo),[Id(i)]))"
		self.assertTrue(TestChecker.test(input,expect,423))
	def test_24(self):
		"""Simple program: int main() {} """
		input = """
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						a[2.1]:=2;
						while(2>1)do
							return;
					end
					"""
		expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.1))"
		self.assertTrue(TestChecker.test(input,expect,424))
	def test_25(self):
		"""Simple program: int main() {} """
		input = """
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						i[2.1]:=2;
						while(2>1)do
							return;
					end
					"""
		expect = "Type Mismatch In Expression: ArrayCell(Id(i),FloatLiteral(2.1))"
		self.assertTrue(TestChecker.test(input,expect,425))
	def test_26(self):
		"""Simple program: int main() {} """
		input = """
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						a[-2+2]:="STR";
						while(2>1)do
							return;
					end
					"""
		expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),BinaryOp(+,UnaryOp(-,IntLiteral(2)),IntLiteral(2))),StringLiteral(STR))"
		self.assertTrue(TestChecker.test(input,expect,426))
	def test_27(self):
		"""Simple program: int main() {} """
		input = """
		function aaa():integer;
		begin
			return 0;
		end
		function foo():integer;
		var i:real;
		begin
			i:=aaa()*2.1*foo();
			return i;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						while(2>1)do
							return;
					end
					"""
		expect = "Type Mismatch In Statement: Return(Some(Id(i)))"
		self.assertTrue(TestChecker.test(input,expect,427))
	def test_28(self):
		"""Simple program: int main() {} """
		input = """
		function foo(a: array[1 .. 2]of integer;b:integer):integer;
		begin
			return a[0]*b;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 3] of integer; 
					begin
						a[1]:=foo(a,2);
					end
					"""
		expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),IntLiteral(2)])"
		self.assertTrue(TestChecker.test(input,expect,428))
	def test_29(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			return;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 3] of integer; 
					begin
						foo(a,2);
					end
					"""
		expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(a),IntLiteral(2)])"
		self.assertTrue(TestChecker.test(input,expect,429))
	def test_30(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			while(2)do
			return;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						foo(a,2);
					end
					"""
		expect = "Type Mismatch In Statement: While(IntLiteral(2),[Return(None)])"
		self.assertTrue(TestChecker.test(input,expect,430))
	def test_31(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			while((2 or 3)+1)do
			return;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						foo(a,2);
					end
					"""
		expect = "Type Mismatch In Expression: BinaryOp(or,IntLiteral(2),IntLiteral(3))"
		self.assertTrue(TestChecker.test(input,expect,431))
	def test_32(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			while(2 + (1 and then 3))do
			return;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						foo(a,2);
					end
					"""
		expect = "Type Mismatch In Expression: BinaryOp(andthen,IntLiteral(1),IntLiteral(3))"
		self.assertTrue(TestChecker.test(input,expect,432))
	def test_33(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			return;
		end
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			return;
		end
		procedure main();
					var i:integer;
					a:array [1 .. 2] of integer; 
					begin
						foo(a,2);
					end
		var s:integer;
					"""
		expect = "Redeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,433))
	def test_34(self):
		"""Simple program: int main() {} """
		input = """
		procedure foo(a: array[1 .. 2]of integer;b:integer);
		begin
			return;
		end
		procedure main(a:integer);begin end
					"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,434))
	def test_35(self):
		"""Simple program: int main() {} """
		input = """
		procedure main();
		var i:real;
		begin
			with i:integer; do
			i:=2.1;
		end
					"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(i),FloatLiteral(2.1))"
		self.assertTrue(TestChecker.test(input,expect,435))
	def test_mismathc166(self):
		"""More complex program"""
		input = """
		var x: array [1 .. 2] of integer;var c:real;var d:integer;
		function main1():   integer;
		begin return 1; end
		function main (): real;var e:integer ; begin
		   return 1;
		end
		"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,436))
	def test_mismathc167(self):
		"""More complex program"""
		input = """
		procedure Main32( c: real);	  
		var Main32: real;	   //2			   
		begin 
				if true then Main32(1);   
		end
		procedure Main( ); var c: real ;	  
			  
		begin   
		end
		"""
		expect = "Undeclared Procedure: Main32"
		self.assertTrue(TestChecker.test(input,expect,437))
	def test_18_if(self):
		"""Blank if statement"""
		input = """function f():real; begin
		if (2.1>2.0) then
			
			begin
			return 2.0;
			end
			return 3.0;
		end"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,438))

	def test_19_if(self):
		"""Add statement"""
		input = """function f(x:integer;y:real):real; begin
		if (x>y) then
			begin
				return f(x<y);
			end
			return .00;
		end
		procedure main();begin end"""
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[BinaryOp(<,Id(x),Id(y))])"
		self.assertTrue(TestChecker.test(input,expect,439))

	def test_20_if(self):
		"""Add blank else"""
		input = """function f():real; begin
		if (True) then
			begin
				return 2.1;
			end
		else begin end
		end
		procedure main();begin end"""
		expect = "Function fNot Return "
		self.assertTrue(TestChecker.test(input,expect,440))

	def test_21_if(self):
		"""Add else statement"""
		input = """function f(x:Boolean):real; begin
		if (x) then
			begin
				f(x);
			end
		else
			begin
				x:=True;
			end
			return .0;
		end
		procedure main();begin end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,441))

	def test_22_if(self):
		"""Nested if"""
		input = """procedure Main(); begin
		if (1+True) then
			if (True) then
				begin end
			else PutIntLn(2);
		end"""
		expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))"
		self.assertTrue(TestChecker.test(input,expect,442))

	def test_23_if(self):
		"""Nested if"""
		input = """procedure MaIn(); begin
		if (x) then
			if (x) then
				begin end
			else begin end
		else PutIntLn(2);
		end"""
		expect = "Undeclared Identifier: x"
		self.assertTrue(TestChecker.test(input,expect,443))

	def test_24_while(self):
		"""Blank while loop"""
		input = """procedure main();
		begin
			while (not 2) do begin end
		end"""
		expect = "Type Mismatch In Expression: UnaryOp(not,IntLiteral(2))"
		self.assertTrue(TestChecker.test(input,expect,444))

	def test_25_while(self):
		"""Add statement"""
		input = """procedure main();
		begin
			while (1+1) do return;
		end"""
		expect = "Type Mismatch In Statement: While(BinaryOp(+,IntLiteral(1),IntLiteral(1)),[Return(None)])"
		self.assertTrue(TestChecker.test(input,expect,445))

	def test_26_for(self):
		"""Blank for loop"""
		input = """procedure main();
		begin
			for i:=-0 to 0 do begin end
		end"""
		expect = "Undeclared Identifier: i"
		self.assertTrue(TestChecker.test(input,expect,446))

	def test_27_for(self):
		"""Add statement"""
		input = """procedure main();
		begin
			for i:=1 to 2 do return;
		end"""
		expect = "Undeclared Identifier: i"
		self.assertTrue(TestChecker.test(input,expect,447))

	def test_28_break(self):
		"""Add break"""
		input = """procedure main();
		begin
			while (1) do begin
				break;
			end
		end"""
		expect = "Type Mismatch In Statement: While(IntLiteral(1),[Break])"
		self.assertTrue(TestChecker.test(input,expect,448))
	def test_all_3(self):
		input = """
				function foo(a:integer; b:boolean):real;
				beGin
					if a = 2 then return 2;					
					return 1;
				end
				procedure main();
				var a: array[0 .. -1] of integer; x:real; y :integer;
				beGin
					if(not not false and then (x >= 4)) then
					begin
						x := foo(a[y + 2], False)[x+y];
					end
				eND
				"""
		expect = "Type Mismatch In Expression: " + str(ArrayCell(CallExpr(Id("foo"),[ArrayCell(Id("a"),BinaryOp("+",Id("y"),IntLiteral(2))),BooleanLiteral(False)]),BinaryOp("+", Id("x"),Id("y"))))
		self.assertTrue(TestChecker.test(input,expect,448))
	def test_all_4(self):
		input = """
				procedure main() ;
				var
					i,j,temp: integer;
				beGin
					With x:integer; do
					beGin
						if(not(false)) then x := x + 2;
						for x:=a[1] downto -32 do
							return;
					end
				eND
				"""
		expect = "Undeclared Identifier: a"
		self.assertTrue(TestChecker.test(input,expect,449))
	
	def test_all_5(self):
		input = """
				procedure main() ;
				var a: array[-3 .. -1] of integer;
				 i,j,temp: integer;
				beGin
					a[i*j] := temp;
					if a then return;
				end
				var a:boolean;
				var b: string;
				"""
		expect = "Type Mismatch In Statement: " + str(If(Id("a"),[Return()],[]))
		self.assertTrue(TestChecker.test(input,expect,450))
	
	def test_all_55(self):
		input = """
				procedure main() ;
				var a: array[0 .. 1] of integer;
				 i,j,temp: integer;
				beGin
					if(true and then a[0]*i + j > 2) then x := x + 2;
				eND
				"""
		expect = "Undeclared Identifier: x"
		self.assertTrue(TestChecker.test(input,expect,451))
	
	def test_all_555(self):
		input = """
				procedure main() ;
				var a: array[0 .. -1] of integer;
				 i,j,temp: integer;
				beGin
					for i := 0 to temp - 2 do
						for j:= i+1 to temp-1 do
							if(a[i]>a[j]) then beGin
								temp := a[i];
								a[i] := a[j];
								a[j] := temp;
							eND
					putInt(a);
				eND
				"""
		expect = "Type Mismatch In Statement: " +str(CallStmt(Id("putInt"),[Id("a")]))
		self.assertTrue(TestChecker.test(input,expect,455))
	
	def test_all_6(self):
		input = """
				Function aaaa(N:array[1 .. 2] of integer) :Integer;
				Var i:Integer;
				Begin
				 For i:= N[i] to 0 do
				  If(N[i] mod i = 0) then
					return 1;
				  Else
					return 2;
				End
				procedure main();
				begin
				end
				"""
		expect = "Function aaaaNot Return "
		self.assertTrue(TestChecker.test(input,expect,456))
	
	def test_all_7(self):
		input = """
				Function kt (A:real;  N:Integer; k:Integer):Boolean;
				Var flag :boolean;
				i :Integer;
				Begin
				 for i:=1 to N do
					 if(A <> A + k) then
					  flag:=false;	 // Cham dut, ket qua: khong phai
				 return flag; {Ket qua kiem tra la mang cap so cong}
				End
				procedure main();
				begin
				return kt();
				end
				"""
		expect = "Type Mismatch In Statement: Return(Some(CallExpr(Id(kt),[])))"
		self.assertTrue(TestChecker.test(input,expect,503))
	
	def test_all_8(self):
		input = """
				Function adsa ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
				Var Flag : Boolean;
				 i :Integer;
				Begin
				 Flag := True;
				 i:= 0;
				 while(i<N) do begin
				  If(A[i] < A[i-1]) Then
				   Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
				  i:=i+1;
				 end
				 return Flag;
				End
				procedure main();
				begin
				return adsa();
				end
				"""
		expect = "Type Mismatch In Statement: Return(Some(CallExpr(Id(adsa),[])))"
		self.assertTrue(TestChecker.test(input,expect,500))
	
	def test_all_9(self):
		input = """
				function call1(i:integer): array[1 .. -4] of real;
				var a: array[1 .. -4] of real;
				begin
					return a;
				end
				procedure gt(x:boolean);
				begin
					if call1(1)[2] <> 2 then
					begin
						if((call1(1)[1] = 2) and x) then 
							while(call1(1)[1] >= 2 and then call1(1)[2] <= 3) do
							beGin
								with a,b:string; do
									break;
							end
					eND
				end
				procedure main();
				begin
					gt(True);
					gt();
				end
				"""
		expect = "Type Mismatch In Statement: CallStmt(Id(gt),[])"
		self.assertTrue(TestChecker.test(input,expect,501))
	
	def test_all_10(self):
		input = """
				function gt(x:boolean): boolean;
				var c:real;
				begin
				while true do
				begin
					if c = 0 then
						continuE;
					else
						return x and then gt(x and x or x);
				end
				end
				procedure main();
				begin
					gt(True);
				end
				"""
		expect = "Function "+ "gt" + "Not Return "
		self.assertTrue(TestChecker.test(input,expect,501))
	
	def test_all_11(self):
		input = """
				procedure a();
				begin
				end
				Procedure ChenPhanTu(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
				Var i :Integer;
				Begin
				 For i:=N downto k+ 1 do
				  A[i] := A[i-1];
				 A[k] := X;
				 a();
				End
				procedure main();
				begin
				ChenPhanTu(True);
				end
				"""
		expect = "Undeclared Procedure: a"
		self.assertTrue(TestChecker.test(input,expect,502))
		
	def test_mismathc168(self):
		"""More complex program"""
		input = """
		function Main32( c: real):real;	  
		var Main32: real;	   //2			   
		begin 
				if true then Main32:=1;   
		end
		procedure Main( ); var c: real ;	  	
		begin   
		end
		"""
		expect = "Function Main32Not Return "
		self.assertTrue(TestChecker.test(input,expect,458))

	def test_mismathc169(self):
		"""More complex program"""
		input = """
		function Main32( c: real):real;	  
		var Main32: real;	   //2			   
		begin 
				return 1  ;
		end
		procedure Main( );   var c: real ;    	
		begin   
			return 1;
		end
		"""
		expect = "Type Mismatch In Statement: Return(Some(IntLiteral(1)))"
		self.assertTrue(TestChecker.test(input,expect,459))

    def test_mismathc171(self):
		"""More complex program"""
		input = """
		function Main32( c: real):real;	  
		var Main32: real;	   //2			   
		begin 
				return 1  ;
		end
		function Main():real;  var c: real ;    	
		begin   
			return 2;
		end
		PROCEDURE Main(); var  c: real;     	
		begin   
			
		end
		"""
		expect = "Redeclared Procedure: Main"
		self.assertTrue(TestChecker.test(input,expect,461))
   
        


    