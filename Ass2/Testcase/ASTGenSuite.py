import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_301(self):
        code = \
        """
            procedure a(); 
			begin
				return;
			end
			function b(): integer;
			begin
				return;
			end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[Return(None)]),FuncDecl(Id(b),[],IntType,[],[Return(None)])])'
        self.assertTrue(TestAST.test(code,expect,301))


    def test_302(self):
        code = \
        """
            procedure a(a,b,c:real; c,e,f:array[1 .. 3] of real);
			begin
				return;
			end
			function a(a,b,c:real; c,e,f:array[1 .. 3] of real): real;
			begin
				return;
			end
        """
        expect = 'Program([FuncDecl(Id(a),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),ArrayType(1,3,FloatType)),VarDecl(Id(e),ArrayType(1,3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))],VoidType(),[],[Return(None)]),FuncDecl(Id(a),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),ArrayType(1,3,FloatType)),VarDecl(Id(e),ArrayType(1,3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))],FloatType,[],[Return(None)])])'
        self.assertTrue(TestAST.test(code,expect,302))


    def test_303(self):
        code = \
        """
			function a(a,b,c:real; c,e,f:array[1 .. 3] of real): array[1 .. -2] of real;
			begin
				return;
			end
        """
        expect = 'Program([FuncDecl(Id(a),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),ArrayType(1,3,FloatType)),VarDecl(Id(e),ArrayType(1,3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))],ArrayType(1,-2,FloatType),[],[Return(None)])])'
        self.assertTrue(TestAST.test(code,expect,303))


    def test_304(self):
        code = \
        """
            procedure a(a,b,c:real; c,e,f:array[1 .. 3] of real);
            var a,b,c: string;
            c,d: array[1 .. -4] of real;
            e,f: integer;
			begin
				return;
			end
			function a(a,b,c:real; c,e,f:array[1 .. 3] of real): real;
            var a,b,c: string;
            c,d: array[1 .. -4] of real;
            e,f: integer; 
			begin
				return;
			end
        """
        expect = 'Program([FuncDecl(Id(a),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),ArrayType(1,3,FloatType)),VarDecl(Id(e),ArrayType(1,3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))],VoidType(),[VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(c),ArrayType(1,-4,FloatType)),VarDecl(Id(d),ArrayType(1,-4,FloatType)),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType)],[Return(None)]),FuncDecl(Id(a),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),ArrayType(1,3,FloatType)),VarDecl(Id(e),ArrayType(1,3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))],FloatType,[VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(c),ArrayType(1,-4,FloatType)),VarDecl(Id(d),ArrayType(1,-4,FloatType)),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType)],[Return(None)])])'
        self.assertTrue(TestAST.test(code,expect,304))


    def test_305(self):
        code = \
        """
            var a: string;
            procedure ma();
            begin
            end
            var c: real;
            function ma(): real;
            begin
            end
        """
        expect = 'Program([VarDecl(Id(a),StringType),FuncDecl(Id(ma),[],VoidType(),[],[]),VarDecl(Id(c),FloatType),FuncDecl(Id(ma),[],FloatType,[],[])])'
        self.assertTrue(TestAST.test(code,expect,305))


    def test_306(self):
        code = \
        """
            var a,b,c: string;
            var d,e,f: real;
            var a:array[-1 .. 2] of real;
            var c:array[-4 .. -3] of real;
            var d:array[2 .. -3] of real;
            var f:array[1 .. 3] of real;
        """
        expect = 'Program([VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType),VarDecl(Id(f),FloatType),VarDecl(Id(a),ArrayType(-1,2,FloatType)),VarDecl(Id(c),ArrayType(-4,-3,FloatType)),VarDecl(Id(d),ArrayType(2,-3,FloatType)),VarDecl(Id(f),ArrayType(1,3,FloatType))])'
        self.assertTrue(TestAST.test(code,expect,306))


    def test_307(self):
        code = \
        """
            procedure main();
            begin
                if a then foo();
                if a then a:=1; else c:=1;
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[CallStmt(Id(foo),[])],[]),If(Id(a),[AssignStmt(Id(a),IntLiteral(1))],[AssignStmt(Id(c),IntLiteral(1))])])])'
        self.assertTrue(TestAST.test(code,expect,307))


    def test_308(self):
        code = \
        """
            procedure main();
            begin
                if a then 
                    begin
                        foo(1,2,4);
                        if b then 
                            begin
                                a := 1;
                                if c then foo(1,2,3); else goo();
                            end
                        else 
                            begin
                                c := 1;
                                foo(1,3);
                            end
                    end
                else 
                    foo();
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(4)]),If(Id(b),[AssignStmt(Id(a),IntLiteral(1)),If(Id(c),[CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])],[CallStmt(Id(goo),[])])],[AssignStmt(Id(c),IntLiteral(1)),CallStmt(Id(foo),[IntLiteral(1),IntLiteral(3)])])],[CallStmt(Id(foo),[])])])])'
        self.assertTrue(TestAST.test(code,expect,308))


    def test_309(self):
        code = \
        """
            procedure main();
            begin
                if a then
                    if b then 
                        if c then 
                            d();
                        else 
                            e();
                    else f();
                else g();
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[If(Id(b),[If(Id(c),[CallStmt(Id(d),[])],[CallStmt(Id(e),[])])],[CallStmt(Id(f),[])])],[CallStmt(Id(g),[])])])])'
        self.assertTrue(TestAST.test(code,expect,309))


    def test_310(self):
        code = \
        """
            procedure main();
            begin
                while (a+b = a[i]) do
                    begin
                        a := 1;
                        foo(1,2,3);
                        return;
                    end
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[While(BinaryOp(=,BinaryOp(+,Id(a),Id(b)),ArrayCell(Id(a),Id(i))),[AssignStmt(Id(a),IntLiteral(1)),CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Return(None)])])])'
        self.assertTrue(TestAST.test(code,expect,310))


    def test_311(self):
        code = \
        """
            procedure main();
            begin
                while (a+b/z) - (1+b*a) <= z do
                    while (a=b) do
                        while (1) do
                            begin
                                return 1;
                            end                        
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[While(BinaryOp(<=,BinaryOp(-,BinaryOp(+,Id(a),BinaryOp(/,Id(b),Id(z))),BinaryOp(+,IntLiteral(1),BinaryOp(*,Id(b),Id(a)))),Id(z)),[While(BinaryOp(=,Id(a),Id(b)),[While(IntLiteral(1),[Return(Some(IntLiteral(1)))])])])])])'
        self.assertTrue(TestAST.test(code,expect,311))


    def test_312(self):
        code = \
        """
            procedure main();
            begin
                for a :=  1+2+a[i] to foo(1,23) do 
                    return 1;
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[For(Id(a)BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),ArrayCell(Id(a),Id(i))),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(23)]),True,[Return(Some(IntLiteral(1)))])])])'
        self.assertTrue(TestAST.test(code,expect,312))


    def test_313(self):
        code = \
        """
            procedure main();
            begin
                for a :=  1+2+a[i] to foo(1,23) do 
                    for a:=1 to 2 do
                        for c:=1 downto 3 do 
                            begin
                                print("asfd");
                                return ;
                            end
            end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[For(Id(a)BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),ArrayCell(Id(a),Id(i))),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(23)]),True,[For(Id(a)IntLiteral(1),IntLiteral(2),True,[For(Id(c)IntLiteral(1),IntLiteral(3),False,[CallStmt(Id(print),[StringLiteral(asfd)]),Return(None)])])])])])'
        self.assertTrue(TestAST.test(code,expect,313))


    def test_314(self):
        code = \
        """
            procedure main();
            begin
                with a,b,c:real; c,e:string; do
                    begin
                        return a+b+c;
                    end
            end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[With([VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(c),StringType),VarDecl(Id(e),StringType)],[Return(Some(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))))])])])'
        self.assertTrue(TestAST.test(code,expect,314))


    def test_315(self):
        code = \
        """
            procedure maiN();
            begin
                with a:real; c:string; do
                    with e:real; e,f:array[1 .. 5] of real; do
                        begin
                        end
            end
        """
        expect = 'Program([FuncDecl(Id(maiN),[],VoidType(),[],[With([VarDecl(Id(a),FloatType),VarDecl(Id(c),StringType)],[With([VarDecl(Id(e),FloatType),VarDecl(Id(e),ArrayType(1,5,FloatType)),VarDecl(Id(f),ArrayType(1,5,FloatType))],[])])])])'
        self.assertTrue(TestAST.test(code,expect,315))


    def test_316(self):
        code = \
        """
            procedure MaIn();
            begin
                a := b := c:= d := foo(1,2,30);
                print("Hello world");
                for i:=1 to 10 do
                    print(i);
                return fo(1,fo());
            end
        """
        expect = 'Program([FuncDecl(Id(MaIn),[],VoidType(),[],[AssignStmt(Id(a),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(30)])),AssignStmt(Id(b),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(30)])),AssignStmt(Id(c),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(30)])),AssignStmt(Id(d),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(30)])),CallStmt(Id(print),[StringLiteral(Hello world)]),For(Id(i)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(print),[Id(i)])]),Return(Some(CallExpr(Id(fo),[IntLiteral(1),CallExpr(Id(fo),[])])))])])'
        self.assertTrue(TestAST.test(code,expect,316))


    def test_317(self):
        code = \
        """
            PROcEdure mmm();
            begin
                a := readln();
                b := readln();
                c := a + b;
                return c;
            end
        """
        expect = 'Program([FuncDecl(Id(mmm),[],VoidType(),[],[AssignStmt(Id(a),CallExpr(Id(readln),[])),AssignStmt(Id(b),CallExpr(Id(readln),[])),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b))),Return(Some(Id(c)))])])'
        self.assertTrue(TestAST.test(code,expect,317))


    def test_318(self):
        code = \
        """
            function ab(a: array[1 .. 3] of real; b: string): array[1 .. 5] of string;
            var a,b,c: string;
            d,e: array[1 .. 4] of string;
            begin
                a[1] := a[2] := a[3] := a[4] := "hello world";
                a:= 1 or else 2;
                b:= 2 and then 1;
                a:= a < b;
                c:= d>b;
                a:= a<=b;
                c:= a>=b;
                e:= a/b;
                e:= a-d;
                e:= a+b;
                e:=a*b;
                e:= a <>b;
                e:= a=b;
                e:= not a + -b;
                e:= not not - not - - not - a;
            end
        """
        expect = 'Program([FuncDecl(Id(ab),[VarDecl(Id(a),ArrayType(1,3,FloatType)),VarDecl(Id(b),StringType)],ArrayType(1,5,StringType),[VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(d),ArrayType(1,4,StringType)),VarDecl(Id(e),ArrayType(1,4,StringType))],[AssignStmt(ArrayCell(Id(a),IntLiteral(1)),StringLiteral(hello world)),AssignStmt(ArrayCell(Id(a),IntLiteral(2)),StringLiteral(hello world)),AssignStmt(ArrayCell(Id(a),IntLiteral(3)),StringLiteral(hello world)),AssignStmt(ArrayCell(Id(a),IntLiteral(4)),StringLiteral(hello world)),AssignStmt(Id(a),BinaryOp(orelse,IntLiteral(1),IntLiteral(2))),AssignStmt(Id(b),BinaryOp(andthen,IntLiteral(2),IntLiteral(1))),AssignStmt(Id(a),BinaryOp(<,Id(a),Id(b))),AssignStmt(Id(c),BinaryOp(>,Id(d),Id(b))),AssignStmt(Id(a),BinaryOp(<=,Id(a),Id(b))),AssignStmt(Id(c),BinaryOp(>=,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(/,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(-,Id(a),Id(d))),AssignStmt(Id(e),BinaryOp(+,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(*,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(<>,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(=,Id(a),Id(b))),AssignStmt(Id(e),BinaryOp(+,UnaryOp(not,Id(a)),UnaryOp(-,Id(b)))),AssignStmt(Id(e),UnaryOp(not,UnaryOp(not,UnaryOp(-,UnaryOp(not,UnaryOp(-,UnaryOp(-,UnaryOp(not,UnaryOp(-,Id(a))))))))))])])'
        self.assertTrue(TestAST.test(code,expect,318))


    def test_319(self):
        code = \
        """
            procedure a(); begin end
            procedure b(); begin end
            var a,b:string;
            var c,d:real;
            function a(): real; begin end
            function b(): string; begin end
            var e,f:integer;
            procedure a(); begin end
            function a(): array[1 .. 2] of string; begin end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[]),FuncDecl(Id(b),[],VoidType(),[],[]),VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),FuncDecl(Id(a),[],FloatType,[],[]),FuncDecl(Id(b),[],StringType,[],[]),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType),FuncDecl(Id(a),[],VoidType(),[],[]),FuncDecl(Id(a),[],ArrayType(1,2,StringType),[],[])])'
        self.assertTrue(TestAST.test(code,expect,319))


    def test_320(self):
        code = \
        """
            procedure a();
            begin
                begin begin begin begin begin end end end end end
            end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[])])'
        self.assertTrue(TestAST.test(code,expect,320))


    def test_321(self):
        code = \
        """
            procedure a();
            begin
                a:= 1.2;
                b:= 2.1e1;
                c:= 1.e-2;
                d:= 3.1e1;
                f:= .4e23;
                g:= -1e-2;
                b:= -3.2e1;
                g:= -1.4e-1;
            end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[AssignStmt(Id(a),FloatLiteral(1.2)),AssignStmt(Id(b),FloatLiteral(21.0)),AssignStmt(Id(c),FloatLiteral(0.01)),AssignStmt(Id(d),FloatLiteral(31.0)),AssignStmt(Id(f),FloatLiteral(4e+22)),AssignStmt(Id(g),UnaryOp(-,FloatLiteral(0.01))),AssignStmt(Id(b),UnaryOp(-,FloatLiteral(32.0))),AssignStmt(Id(g),UnaryOp(-,FloatLiteral(0.14)))])])'
        self.assertTrue(TestAST.test(code,expect,321))


    def test_322(self):
        code = \
        """
            procedure a();
            begin
                f(f(f(f(f(f())))));
            end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[CallStmt(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[])])])])])])])])'
        self.assertTrue(TestAST.test(code,expect,322))


    def test_323(self):
        code = \
        """
            procedure a();
            begin
                a:=a[a[a[a[a[a]]]]];
            end
        """
        expect = 'Program([FuncDecl(Id(a),[],VoidType(),[],[AssignStmt(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),Id(a)))))))])])'
        self.assertTrue(TestAST.test(code,expect,323))


    def test_324(self):
        code = \
        """
        procedure main();
        begin
            a := foo(1+a[i-goo(t*hoo(t[x]))]*6-(a[(2+1)*3]+1)*a[2])[(2-5)+a[x]];
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),ArrayCell(CallExpr(Id(foo),[BinaryOp(-,BinaryOp(+,IntLiteral(1),BinaryOp(*,ArrayCell(Id(a),BinaryOp(-,Id(i),CallExpr(Id(goo),[BinaryOp(*,Id(t),CallExpr(Id(hoo),[ArrayCell(Id(t),Id(x))]))]))),IntLiteral(6))),BinaryOp(*,BinaryOp(+,ArrayCell(Id(a),BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(1)),IntLiteral(3))),IntLiteral(1)),ArrayCell(Id(a),IntLiteral(2))))]),BinaryOp(+,BinaryOp(-,IntLiteral(2),IntLiteral(5)),ArrayCell(Id(a),Id(x)))))])])'
        self.assertTrue(TestAST.test(code,expect,324))


    def test_325(self):
        code = \
        """
        procedure main();
        begin
            a := a[1][2][3];
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),ArrayCell(ArrayCell(ArrayCell(Id(a),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)))])])'
        self.assertTrue(TestAST.test(code,expect,325))


    def test_326(self):
        code = \
        """
        procedure main();
        begin
            a := a[a[a]][a[a[a]]];
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),ArrayCell(Id(a),Id(a))),ArrayCell(Id(a),ArrayCell(Id(a),Id(a)))))])])'
        self.assertTrue(TestAST.test(code,expect,326))


    def test_327(self):
        code = \
        """
        procedure main();
        begin
            a[1] := a[a[a]] := a[a][a] := (a)[a] := a()[a] := a[(a)];
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(a),Id(a))),AssignStmt(ArrayCell(Id(a),ArrayCell(Id(a),Id(a))),ArrayCell(Id(a),Id(a))),AssignStmt(ArrayCell(ArrayCell(Id(a),Id(a)),Id(a)),ArrayCell(Id(a),Id(a))),AssignStmt(ArrayCell(Id(a),Id(a)),ArrayCell(Id(a),Id(a))),AssignStmt(ArrayCell(CallExpr(Id(a),[]),Id(a)),ArrayCell(Id(a),Id(a)))])])'
        self.assertTrue(TestAST.test(code,expect,327))


    def test_328(self):
        code = \
        """
        procedure main();
        begin
            a := not - a + b * -d div 2 mod a >= - not 3 + 4;
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(>=,BinaryOp(+,UnaryOp(not,UnaryOp(-,Id(a))),BinaryOp(mod,BinaryOp(div,BinaryOp(*,Id(b),UnaryOp(-,Id(d))),IntLiteral(2)),Id(a))),BinaryOp(+,UnaryOp(-,UnaryOp(not,IntLiteral(3))),IntLiteral(4))))])])'
        self.assertTrue(TestAST.test(code,expect,328))


    def test_329(self):
        code = \
        """
        procedure main();
        begin
            a := not Not NOT nOt - - - - - a;
        end           
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),UnaryOp(not,UnaryOp(Not,UnaryOp(NOT,UnaryOp(nOt,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a)))))))))))])])'
        self.assertTrue(TestAST.test(code,expect,329))


    def test_330(self):
        code = \
        """
        procedure main();
        begin
            a := ((((((((a+b))))))));
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(+,Id(a),Id(b)))])])'
        self.assertTrue(TestAST.test(code,expect,330))


    def test_331(self):
        code = \
        """
        procedure main();
        begin
            a := (a)div(a)mod(a)/a-a+a*a;
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(/,BinaryOp(mod,BinaryOp(div,Id(a),Id(a)),Id(a)),Id(a)),Id(a)),BinaryOp(*,Id(a),Id(a))))])])'
        self.assertTrue(TestAST.test(code,expect,331))


    def test_332(self):
        code = \
        """
        procedure main();
        begin
            if a then
                if b then
                    if c then
                        f();
                    else g();
                else c();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[If(Id(b),[If(Id(c),[CallStmt(Id(f),[])],[CallStmt(Id(g),[])])],[CallStmt(Id(c),[])])],[])])])'
        self.assertTrue(TestAST.test(code,expect,332))


    def test_333(self):
        code = \
        """
        procedure main();
        begin
            if a then
                if b then
                    if c then
                        f();
                    else g();
                else c();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[If(Id(b),[If(Id(c),[CallStmt(Id(f),[])],[CallStmt(Id(g),[])])],[CallStmt(Id(c),[])])],[])])])'
        self.assertTrue(TestAST.test(code,expect,333))


    def test_334(self):
        code = \
        """
        procedure main();
        begin
            if a then
                begin
                    f(); g();
                end
            else
                if b then
                    f();
                else
                    begin
                        c(); d();
                    end
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[CallStmt(Id(f),[]),CallStmt(Id(g),[])],[If(Id(b),[CallStmt(Id(f),[])],[CallStmt(Id(c),[]),CallStmt(Id(d),[])])])])])'
        self.assertTrue(TestAST.test(code,expect,334))


    def test_335(self):
        code = \
        """
        procedure main();
        begin
            if a then
                if b then
                    if c then
                        if d then
                            e();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[If(Id(a),[If(Id(b),[If(Id(c),[If(Id(d),[CallStmt(Id(e),[])],[])],[])],[])],[])])])'
        self.assertTrue(TestAST.test(code,expect,335))


    def test_336(self):
        code = \
        """
        procedure main();
        begin
            while a do b();
            while a do
                begin
                    c();
                end
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[While(Id(a),[CallStmt(Id(b),[])]),While(Id(a),[CallStmt(Id(c),[])])])])'
        self.assertTrue(TestAST.test(code,expect,336))


    def test_337(self):
        code = \
        """
        procedure main();
        begin
            while a do while b do while c do d();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[While(Id(a),[While(Id(b),[While(Id(c),[CallStmt(Id(d),[])])])])])])'
        self.assertTrue(TestAST.test(code,expect,337))


    def test_338(self):
        code = \
        """
        procedure main();
        begin
            for i:=1 to 2 do c();
            for i:=2 downto 1 do c();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)IntLiteral(1),IntLiteral(2),True,[CallStmt(Id(c),[])]),For(Id(i)IntLiteral(2),IntLiteral(1),False,[CallStmt(Id(c),[])])])])'
        self.assertTrue(TestAST.test(code,expect,338))


    def test_339(self):
        code = \
        """
        procedure main();
        begin
            for i:=a[1] to a[2] do c();
            for i:=foo(a[1]+1)[1] to 1 do c();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(a),IntLiteral(2)),True,[CallStmt(Id(c),[])]),For(Id(i)ArrayCell(CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),IntLiteral(1)),IntLiteral(1))]),IntLiteral(1)),IntLiteral(1),True,[CallStmt(Id(c),[])])])])'
        self.assertTrue(TestAST.test(code,expect,339))


    def test_340(self):
        code = \
        """
        procedure main();
        begin
            for i:=a to b do
                for j:=1 to 2 do
                    for k:=1 to 3 do
                        begin
                            c();
                        end
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)Id(a),Id(b),True,[For(Id(j)IntLiteral(1),IntLiteral(2),True,[For(Id(k)IntLiteral(1),IntLiteral(3),True,[CallStmt(Id(c),[])])])])])])'
        self.assertTrue(TestAST.test(code,expect,340))


    def test_341(self):
        code = \
        """
        procedure main();
        begin
            while 1 do 
                begin
                    break;
                    continue;
                    return;
                end
            return a[1] + 2 * b;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[While(IntLiteral(1),[Break,Continue,Return(None)]),Return(Some(BinaryOp(+,ArrayCell(Id(a),IntLiteral(1)),BinaryOp(*,IntLiteral(2),Id(b)))))])])'
        self.assertTrue(TestAST.test(code,expect,341))


    def test_342(self):
        code = \
        """
        procedure main();
        begin
            foo(1,2,3,4);
            with a,b,c:integer; d:real; e:array[1 .. 2] of boolean; g: string; do
                begin
                    return foo(12,3,a,b);
                end
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),With([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(1,2,BoolType)),VarDecl(Id(g),StringType)],[Return(Some(CallExpr(Id(foo),[IntLiteral(12),IntLiteral(3),Id(a),Id(b)])))])])])'
        self.assertTrue(TestAST.test(code,expect,342))


    def test_343(self):
        code = \
        """
        procedure main();
        begin
            foo(1,2,3,4);
            with a,b,c:integer; d:real; e:array[1 .. 2] of boolean; g: string; do
                begin
                    return foo(12,3,a,b);
                end
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),With([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(1,2,BoolType)),VarDecl(Id(g),StringType)],[Return(Some(CallExpr(Id(foo),[IntLiteral(12),IntLiteral(3),Id(a),Id(b)])))])])])'
        self.assertTrue(TestAST.test(code,expect,343))


    def test_344(self):
        code = \
        """
        procedure main();
        begin
            with a:real; do with b:real; do with c:real; do fo();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[With([VarDecl(Id(a),FloatType)],[With([VarDecl(Id(b),FloatType)],[With([VarDecl(Id(c),FloatType)],[CallStmt(Id(fo),[])])])])])])'
        self.assertTrue(TestAST.test(code,expect,344))


    def test_345(self):
        code = \
        """
        procedure main();
            var h,c: integer;
            j,k: real;
            c: array[1 .. 3] of string;
        begin
            
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(h),IntType),VarDecl(Id(c),IntType),VarDecl(Id(j),FloatType),VarDecl(Id(k),FloatType),VarDecl(Id(c),ArrayType(1,3,StringType))],[])])'
        self.assertTrue(TestAST.test(code,expect,345))


    def test_346(self):
        code = \
        """
        procedure main();
        begin
            print("hello world \\n hello \\t hello \\' hello \\\" hello ");
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(print),[StringLiteral(hello world \\n hello \\t hello \\\' hello \\" hello )])])])'
        self.assertTrue(TestAST.test(code,expect,346))


    def test_347(self):
        code = \
        """
        procedure main();
        begin
            print("!@##%$^#^$&*&(*&*)()+_~,.<?<;:[]{}|");
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(print),[StringLiteral(!@##%$^#^$&*&(*&*)()+_~,.<?<;:[]{}|)])])])'
        self.assertTrue(TestAST.test(code,expect,347))


    def test_348(self):
        code = \
        """
        procedure main();
        begin
            a:= a or b or c or else d;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(orelse,BinaryOp(or,BinaryOp(or,Id(a),Id(b)),Id(c)),Id(d)))])])'
        self.assertTrue(TestAST.test(code,expect,348))


    def test_349(self):
        code = \
        """
        procedure main();
        begin
            f()[f()] := a[f(a[a])];
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(CallExpr(Id(f),[]),CallExpr(Id(f),[])),ArrayCell(Id(a),CallExpr(Id(f),[ArrayCell(Id(a),Id(a))])))])])'
        self.assertTrue(TestAST.test(code,expect,349))


    def test_350(self):
        code = \
        """
        procedure main();
        begin
            true[a] := false[b] := (----a)[a] := 1;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(BooleanLiteral(True),Id(a)),IntLiteral(1)),AssignStmt(ArrayCell(BooleanLiteral(False),Id(b)),IntLiteral(1)),AssignStmt(ArrayCell(UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a))))),Id(a)),IntLiteral(1))])])'
        self.assertTrue(TestAST.test(code,expect,350))


    def test_351(self):
        code = \
        """
        procedure main();
        begin
            foo()[1] := 1;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(CallExpr(Id(foo),[]),IntLiteral(1)),IntLiteral(1))])])'
        self.assertTrue(TestAST.test(code,expect,351))


    def test_352(self):
        code = \
        """
        procedure main();
        begin
            f()[1] := f[2] := f(20)[2] := f(2[2])[1] :=1;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(CallExpr(Id(f),[]),IntLiteral(1)),IntLiteral(1)),AssignStmt(ArrayCell(Id(f),IntLiteral(2)),IntLiteral(1)),AssignStmt(ArrayCell(CallExpr(Id(f),[IntLiteral(20)]),IntLiteral(2)),IntLiteral(1)),AssignStmt(ArrayCell(CallExpr(Id(f),[ArrayCell(IntLiteral(2),IntLiteral(2))]),IntLiteral(1)),IntLiteral(1))])])'
        self.assertTrue(TestAST.test(code,expect,352))


    def test_353(self):
        code = \
        """
        procedure main();
        begin
            f("a")["b"] := c("");
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(ArrayCell(CallExpr(Id(f),[StringLiteral(a)]),StringLiteral(b)),CallExpr(Id(c),[StringLiteral()]))])])'
        self.assertTrue(TestAST.test(code,expect,353))


    def test_354(self):
        code = \
        """
        procedure main();
        begin
            T:= true = false;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(T),BinaryOp(=,BooleanLiteral(True),BooleanLiteral(False)))])])'
        self.assertTrue(TestAST.test(code,expect,354))


    def test_355(self):
        code = \
        """
        procedure main();
        begin
            a := a and              then 1;
            c := 1 or          else 2;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(andthen,Id(a),IntLiteral(1))),AssignStmt(Id(c),BinaryOp(orelse,IntLiteral(1),IntLiteral(2)))])])'
        self.assertTrue(TestAST.test(code,expect,355))


    def test_356(self):
        code = \
        """
        procedure main();
        begin
            a:= - not - a;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),UnaryOp(-,UnaryOp(not,UnaryOp(-,Id(a)))))])])'
        self.assertTrue(TestAST.test(code,expect,356))


    def test_357(self):
        code = \
        """
        procedure main();
        begin
            a := b DiV a MoD c AnD ThEn b;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(andthen,BinaryOp(MoD,BinaryOp(DiV,Id(b),Id(a)),Id(c)),Id(b)))])])'
        self.assertTrue(TestAST.test(code,expect,357))


    def test_358(self):
        code = \
        """
        procedure main();
        begin
            a := TRue <> FaLSe;
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(a),BinaryOp(<>,BooleanLiteral(True),BooleanLiteral(False)))])])'
        self.assertTrue(TestAST.test(code,expect,358))


    def test_359(self):
        code = \
        """
        procedure main();
        begin
            this_is_very_long_name := VarDecl(Float(), Id("abc"));
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(this_is_very_long_name),CallExpr(Id(VarDecl),[CallExpr(Id(Float),[]),CallExpr(Id(Id),[StringLiteral(abc)])]))])])'
        self.assertTrue(TestAST.test(code,expect,359))


    def test_360(self):
        code = \
        """
        procedure main();
        begin
            
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[])])'
        self.assertTrue(TestAST.test(code,expect,360))


    def test_361(self):
        code = \
        """
        var i, j:integer;

        procedure main();
        begin
            for i := 2 to 50 do
        
            begin
                for j := 2 to i do
                    if (i mod j)=0  then
                        break; {* if factor found, not prime *}
                
                if(j = i) then
                    writeln(i , " is prime" );
            end
        end
        """
        expect = 'Program([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),FuncDecl(Id(main),[],VoidType(),[],[For(Id(i)IntLiteral(2),IntLiteral(50),True,[For(Id(j)IntLiteral(2),Id(i),True,[If(BinaryOp(=,BinaryOp(mod,Id(i),Id(j)),IntLiteral(0)),[Break],[])]),If(BinaryOp(=,Id(j),Id(i)),[CallStmt(Id(writeln),[Id(i),StringLiteral( is prime)])],[])])])])'
        self.assertTrue(TestAST.test(code,expect,361))


    def test_362(self):
        code = \
        """
        procedure operators();
        begin
            clrscr();
            writeln(17 div 3);
            readln();
            writeln(7 mod 4);
            readln();
        end
        """
        expect = 'Program([FuncDecl(Id(operators),[],VoidType(),[],[CallStmt(Id(clrscr),[]),CallStmt(Id(writeln),[BinaryOp(div,IntLiteral(17),IntLiteral(3))]),CallStmt(Id(readln),[]),CallStmt(Id(writeln),[BinaryOp(mod,IntLiteral(7),IntLiteral(4))]),CallStmt(Id(readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,362))


    def test_363(self):
        code = \
        """
        procedure posneg();
        var 
        no : integer;
        begin
        clrscr();
        Write("Enger a number:");
        readln(no);
        if (no > 0) then
            writeln("You enter Positive Number");
        else
            if (no < 0) then
                writeln("You enter Negative number");
            else 
                if (no = 0) then
                    writeln("You enter Zero");
        readln();
        end
        """
        expect = 'Program([FuncDecl(Id(posneg),[],VoidType(),[VarDecl(Id(no),IntType)],[CallStmt(Id(clrscr),[]),CallStmt(Id(Write),[StringLiteral(Enger a number:)]),CallStmt(Id(readln),[Id(no)]),If(BinaryOp(>,Id(no),IntLiteral(0)),[CallStmt(Id(writeln),[StringLiteral(You enter Positive Number)])],[If(BinaryOp(<,Id(no),IntLiteral(0)),[CallStmt(Id(writeln),[StringLiteral(You enter Negative number)])],[If(BinaryOp(=,Id(no),IntLiteral(0)),[CallStmt(Id(writeln),[StringLiteral(You enter Zero)])],[])])]),CallStmt(Id(readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,363))


    def test_364(self):
        code = \
        """
        procedure lights();
        var a,b:integer;
        begin
        textbackground(white);
        clrscr();
        for a:=1 to 1000000 do inc(b);
        randomize();
        
        a:=random(4)+1;
        if a=1 then textbackground(blue);
        if a=2 then textbackground(red);
        if a=3 then textbackground(green);
        if a=4 then textbackground(yellow);
        write();
        goto(1);
        end
        """
        expect = 'Program([FuncDecl(Id(lights),[],VoidType(),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],[CallStmt(Id(textbackground),[Id(white)]),CallStmt(Id(clrscr),[]),For(Id(a)IntLiteral(1),IntLiteral(1000000),True,[CallStmt(Id(inc),[Id(b)])]),CallStmt(Id(randomize),[]),AssignStmt(Id(a),BinaryOp(+,CallExpr(Id(random),[IntLiteral(4)]),IntLiteral(1))),If(BinaryOp(=,Id(a),IntLiteral(1)),[CallStmt(Id(textbackground),[Id(blue)])],[]),If(BinaryOp(=,Id(a),IntLiteral(2)),[CallStmt(Id(textbackground),[Id(red)])],[]),If(BinaryOp(=,Id(a),IntLiteral(3)),[CallStmt(Id(textbackground),[Id(green)])],[]),If(BinaryOp(=,Id(a),IntLiteral(4)),[CallStmt(Id(textbackground),[Id(yellow)])],[]),CallStmt(Id(write),[]),CallStmt(Id(goto),[IntLiteral(1)])])])'
        self.assertTrue(TestAST.test(code,expect,364))


    def test_365(self):
        code = \
        """
        procedure learn();
        var a,b,c,e,f,right: integer; d:real;
        begin
            textbackground(green);
            textcolor(white);
            e:=random(3)+1;
            b:=random(200)+1;
            c:=random(200)+1;
            if e=1 then d:=b+c;
            if e=2 then d:=b-c;
            if e=3 then d:=b*c;
            writeln(" ",b/3);
            if e=1 then write("+ ");  
            if e=2 then write("- ");
            if e=3 then write("x ");
            writeln(c/3);
            writeln("______");
            readln(a);
            if a=d then
                begin                                       
                    inc(right);
                    writeln("HORRAY! YOU GOT IT RIGHT! you have ",right," points!");
                end
            else
                begin
                    right:=right-1;
                    writeln("WRONG! you have ",right," points");
                end
        end
        """
        expect = 'Program([FuncDecl(Id(learn),[],VoidType(),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType),VarDecl(Id(right),IntType),VarDecl(Id(d),FloatType)],[CallStmt(Id(textbackground),[Id(green)]),CallStmt(Id(textcolor),[Id(white)]),AssignStmt(Id(e),BinaryOp(+,CallExpr(Id(random),[IntLiteral(3)]),IntLiteral(1))),AssignStmt(Id(b),BinaryOp(+,CallExpr(Id(random),[IntLiteral(200)]),IntLiteral(1))),AssignStmt(Id(c),BinaryOp(+,CallExpr(Id(random),[IntLiteral(200)]),IntLiteral(1))),If(BinaryOp(=,Id(e),IntLiteral(1)),[AssignStmt(Id(d),BinaryOp(+,Id(b),Id(c)))],[]),If(BinaryOp(=,Id(e),IntLiteral(2)),[AssignStmt(Id(d),BinaryOp(-,Id(b),Id(c)))],[]),If(BinaryOp(=,Id(e),IntLiteral(3)),[AssignStmt(Id(d),BinaryOp(*,Id(b),Id(c)))],[]),CallStmt(Id(writeln),[StringLiteral( ),BinaryOp(/,Id(b),IntLiteral(3))]),If(BinaryOp(=,Id(e),IntLiteral(1)),[CallStmt(Id(write),[StringLiteral(+ )])],[]),If(BinaryOp(=,Id(e),IntLiteral(2)),[CallStmt(Id(write),[StringLiteral(- )])],[]),If(BinaryOp(=,Id(e),IntLiteral(3)),[CallStmt(Id(write),[StringLiteral(x )])],[]),CallStmt(Id(writeln),[BinaryOp(/,Id(c),IntLiteral(3))]),CallStmt(Id(writeln),[StringLiteral(______)]),CallStmt(Id(readln),[Id(a)]),If(BinaryOp(=,Id(a),Id(d)),[CallStmt(Id(inc),[Id(right)]),CallStmt(Id(writeln),[StringLiteral(HORRAY! YOU GOT IT RIGHT! you have ),Id(right),StringLiteral( points!)])],[AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1))),CallStmt(Id(writeln),[StringLiteral(WRONG! you have ),Id(right),StringLiteral( points)])])])])'
        self.assertTrue(TestAST.test(code,expect,365))


    def test_366(self):
        code = \
        """
        procedure Lesson1_Program3();
        Var       
            Num1, Num2, Sum : Integer;

        Begin {no semicolon}
            Write("Input number 1:"); 
            Readln(Num1);
            Writeln("Input number 2:");
            Readln(Num2);
            Sum := Num1 + Num2; {addition} 
            Writeln(Sum);
            Readln();
        End
        """
        expect = 'Program([FuncDecl(Id(Lesson1_Program3),[],VoidType(),[VarDecl(Id(Num1),IntType),VarDecl(Id(Num2),IntType),VarDecl(Id(Sum),IntType)],[CallStmt(Id(Write),[StringLiteral(Input number 1:)]),CallStmt(Id(Readln),[Id(Num1)]),CallStmt(Id(Writeln),[StringLiteral(Input number 2:)]),CallStmt(Id(Readln),[Id(Num2)]),AssignStmt(Id(Sum),BinaryOp(+,Id(Num1),Id(Num2))),CallStmt(Id(Writeln),[Id(Sum)]),CallStmt(Id(Readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,366))


    def test_367(self):
        code = \
        """
        procedure one(); 
        var P : String;  
        begin  
        P := "This is a null-terminated string.";  
        WriteLn (P);  
        end
        """
        expect = 'Program([FuncDecl(Id(one),[],VoidType(),[VarDecl(Id(P),StringType)],[AssignStmt(Id(P),StringLiteral(This is a null-terminated string.)),CallStmt(Id(WriteLn),[Id(P)])])])'
        self.assertTrue(TestAST.test(code,expect,367))


    def test_368(self):
        code = \
        """
        Procedure InsertionSort(numbers : Array[1 .. 2] of Integer; size : Integer);
        Var
            i, j, index : Integer;


        Begin
            For i := 2 to size-1 do
            Begin
                index := numbers[i];
                j := i;
                While ((j > 1) AND (numbers[j-1] > index)) do
                Begin
                    numbers[j] := numbers[j-1];
                    j := j - 1;
                End
                numbers[j] := index;
            End
        End
        """
        expect = 'Program([FuncDecl(Id(InsertionSort),[VarDecl(Id(numbers),ArrayType(1,2,IntType)),VarDecl(Id(size),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(index),IntType)],[For(Id(i)IntLiteral(2),BinaryOp(-,Id(size),IntLiteral(1)),True,[AssignStmt(Id(index),ArrayCell(Id(numbers),Id(i))),AssignStmt(Id(j),Id(i)),While(BinaryOp(AND,BinaryOp(>,Id(j),IntLiteral(1)),BinaryOp(>,ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1))),Id(index))),[AssignStmt(ArrayCell(Id(numbers),Id(j)),ArrayCell(Id(numbers),BinaryOp(-,Id(j),IntLiteral(1)))),AssignStmt(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))]),AssignStmt(ArrayCell(Id(numbers),Id(j)),Id(index))])])])'
        self.assertTrue(TestAST.test(code,expect,368))


    def test_369(self):
        code = \
        """
        Procedure QSort(numbers : Array[1 .. 2] of Integer; left : Integer; right : Integer);
        Var 
            pivot, l_ptr, r_ptr : Integer;

        Begin
            l_ptr := left;
            r_ptr := right;
            pivot := numbers[left];

            While (left < right) do
            Begin
                While ((numbers[right] >= pivot) AND (left < right)) do
                    right := right - 1;

                If (left <> right) Then
                Begin
                    numbers[left] := numbers[right];
                    left := left + 1;
                End

                While ((numbers[left] <= pivot) AND (left < right)) do
                    left := left + 1;

                If (left <> right) Then
                Begin
                    numbers[right] := numbers[left];
                    right := right - 1;
                End
            End

            numbers[left] := pivot;
            pivot := left;
            left := l_ptr;
            right := r_ptr;

            If (left < pivot) Then
                QSort(numbers, left, pivot-1);

            If (right > pivot) Then
                QSort(numbers, pivot+1, right);
        End

        Procedure QuickSort(numbers : Array[1 .. 2] of Integer; size : Integer);
        Begin
            QSort(numbers, 0, size-1);
        End
        """
        expect = 'Program([FuncDecl(Id(QSort),[VarDecl(Id(numbers),ArrayType(1,2,IntType)),VarDecl(Id(left),IntType),VarDecl(Id(right),IntType)],VoidType(),[VarDecl(Id(pivot),IntType),VarDecl(Id(l_ptr),IntType),VarDecl(Id(r_ptr),IntType)],[AssignStmt(Id(l_ptr),Id(left)),AssignStmt(Id(r_ptr),Id(right)),AssignStmt(Id(pivot),ArrayCell(Id(numbers),Id(left))),While(BinaryOp(<,Id(left),Id(right)),[While(BinaryOp(AND,BinaryOp(>=,ArrayCell(Id(numbers),Id(right)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(left)),ArrayCell(Id(numbers),Id(right))),AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))],[]),While(BinaryOp(AND,BinaryOp(<=,ArrayCell(Id(numbers),Id(left)),Id(pivot)),BinaryOp(<,Id(left),Id(right))),[AssignStmt(Id(left),BinaryOp(+,Id(left),IntLiteral(1)))]),If(BinaryOp(<>,Id(left),Id(right)),[AssignStmt(ArrayCell(Id(numbers),Id(right)),ArrayCell(Id(numbers),Id(left))),AssignStmt(Id(right),BinaryOp(-,Id(right),IntLiteral(1)))],[])]),AssignStmt(ArrayCell(Id(numbers),Id(left)),Id(pivot)),AssignStmt(Id(pivot),Id(left)),AssignStmt(Id(left),Id(l_ptr)),AssignStmt(Id(right),Id(r_ptr)),If(BinaryOp(<,Id(left),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),Id(left),BinaryOp(-,Id(pivot),IntLiteral(1))])],[]),If(BinaryOp(>,Id(right),Id(pivot)),[CallStmt(Id(QSort),[Id(numbers),BinaryOp(+,Id(pivot),IntLiteral(1)),Id(right)])],[])]),FuncDecl(Id(QuickSort),[VarDecl(Id(numbers),ArrayType(1,2,IntType)),VarDecl(Id(size),IntType)],VoidType(),[],[CallStmt(Id(QSort),[Id(numbers),IntLiteral(0),BinaryOp(-,Id(size),IntLiteral(1))])])])'
        self.assertTrue(TestAST.test(code,expect,369))


    def test_370(self):
        code = \
        """
        procedure Lesson2_Program1();
        Var name, surname: String;
            
        Begin
            write("Enter your name:");
            readln(name);
            write("Enter your surname:");
            readln(surname);
            writeln();{new line}
            writeln();{new line}
            writeln("Your full name is: ",name," ",surname);
            readln();
        End
        """
        expect = 'Program([FuncDecl(Id(Lesson2_Program1),[],VoidType(),[VarDecl(Id(name),StringType),VarDecl(Id(surname),StringType)],[CallStmt(Id(write),[StringLiteral(Enter your name:)]),CallStmt(Id(readln),[Id(name)]),CallStmt(Id(write),[StringLiteral(Enter your surname:)]),CallStmt(Id(readln),[Id(surname)]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[]),CallStmt(Id(writeln),[StringLiteral(Your full name is: ),Id(name),StringLiteral( ),Id(surname)]),CallStmt(Id(readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,370))


    def test_371(self):
        code = \
        """
        procedure main();
        Var
            myVar : Integer;
            myArray : Array[1 .. 5] of Integer;
            
        Begin
            myArray[2] := 25;
            myVar := myArray[2];
        End
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(myVar),IntType),VarDecl(Id(myArray),ArrayType(1,5,IntType))],[AssignStmt(ArrayCell(Id(myArray),IntLiteral(2)),IntLiteral(25)),AssignStmt(Id(myVar),ArrayCell(Id(myArray),IntLiteral(2)))])])'
        self.assertTrue(TestAST.test(code,expect,371))


    def test_372(self):
        code = \
        """
        procedure main();
        Var
            i : Integer;
            myIntArray : Array[1 .. 20] of Integer;
            myBoolArray : Array[1 .. 20] of Boolean;

        Begin
            For i := 1 to Length(myIntArray) do
            Begin
                myIntArray[i] := 1;
                myBoolArray[i] := True;
            End
        End
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(myIntArray),ArrayType(1,20,IntType)),VarDecl(Id(myBoolArray),ArrayType(1,20,BoolType))],[For(Id(i)IntLiteral(1),CallExpr(Id(Length),[Id(myIntArray)]),True,[AssignStmt(ArrayCell(Id(myIntArray),Id(i)),IntLiteral(1)),AssignStmt(ArrayCell(Id(myBoolArray),Id(i)),BooleanLiteral(True))])])])'
        self.assertTrue(TestAST.test(code,expect,372))


    def test_373(self):
        code = \
        """
        procedure main();
        Var
            name : integer;
            age  : integer;

        Begin
            Write("Enter your name: ");
            Readln(name);
            Write("Enter your age: ");
            Readln(age);
            Writeln();
            Writeln("Your name:", name);
            Writeln("Your age :", age);
            Readln();
        End
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(name),IntType),VarDecl(Id(age),IntType)],[CallStmt(Id(Write),[StringLiteral(Enter your name: )]),CallStmt(Id(Readln),[Id(name)]),CallStmt(Id(Write),[StringLiteral(Enter your age: )]),CallStmt(Id(Readln),[Id(age)]),CallStmt(Id(Writeln),[]),CallStmt(Id(Writeln),[StringLiteral(Your name:),Id(name)]),CallStmt(Id(Writeln),[StringLiteral(Your age :),Id(age)]),CallStmt(Id(Readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,373))


    def test_374(self):
        code = \
        """
        procedure main();
        Begin
            Writeln("Please enter 5 numbers from (0..255): ");
            
            For i := 1 to Length(myArrayVar) do
                Readln(myArrayVar[i]);
            
            Writeln("You have entered the following numbers: ");
            
            For i := 1 to Length(myArrayVar)do
                Writeln("Number ",i,": ",myArrayVar[i]);
            
            Writeln("Now writing them to file...");   {store the numbers in a file}
            Assign(myFile, "example.dat");
            ReWrite(byteFile);
            Write(myFile, myArrayVar[i]);
            Close(myFile);
            Writeln("Done, you may exit..");
            Readln();
        End 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Writeln),[StringLiteral(Please enter 5 numbers from (0..255): )]),For(Id(i)IntLiteral(1),CallExpr(Id(Length),[Id(myArrayVar)]),True,[CallStmt(Id(Readln),[ArrayCell(Id(myArrayVar),Id(i))])]),CallStmt(Id(Writeln),[StringLiteral(You have entered the following numbers: )]),For(Id(i)IntLiteral(1),CallExpr(Id(Length),[Id(myArrayVar)]),True,[CallStmt(Id(Writeln),[StringLiteral(Number ),Id(i),StringLiteral(: ),ArrayCell(Id(myArrayVar),Id(i))])]),CallStmt(Id(Writeln),[StringLiteral(Now writing them to file...)]),CallStmt(Id(Assign),[Id(myFile),StringLiteral(example.dat)]),CallStmt(Id(ReWrite),[Id(byteFile)]),CallStmt(Id(Write),[Id(myFile),ArrayCell(Id(myArrayVar),Id(i))]),CallStmt(Id(Close),[Id(myFile)]),CallStmt(Id(Writeln),[StringLiteral(Done, you may exit..)]),CallStmt(Id(Readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,374))


    def test_375(self):
        code = \
        """
        procedure main();
        Var
            i        : integer;
            myFile   : integer; { the next array is 2 dimensional }
            arrayInt : Array[1 .. 2] of integer;
        
        Begin
            Clrscr();
            Randomize();
            
            For i := 1 to 5 do { or we can use Length(arrayInt[1][i]) }
            Begin
                arrayInt[1][i] := Random(1000);
                Writeln("rand num: ",arrayInt[1][i]);
            End

            Assign(myFile, "test.dat");
            ReWrite(myFile);
            Write(myFile, arrayInt[1]);
            Close(myFile);
            ReSet(myFile);
            Read(myFile, arrayInt[2]);
            Close(myFile);

            For i := 1 to 5 do
                Writeln(i,": ", arrayInt[2][i]);

            Readln();
        End 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(myFile),IntType),VarDecl(Id(arrayInt),ArrayType(1,2,IntType))],[CallStmt(Id(Clrscr),[]),CallStmt(Id(Randomize),[]),For(Id(i)IntLiteral(1),IntLiteral(5),True,[AssignStmt(ArrayCell(ArrayCell(Id(arrayInt),IntLiteral(1)),Id(i)),CallExpr(Id(Random),[IntLiteral(1000)])),CallStmt(Id(Writeln),[StringLiteral(rand num: ),ArrayCell(ArrayCell(Id(arrayInt),IntLiteral(1)),Id(i))])]),CallStmt(Id(Assign),[Id(myFile),StringLiteral(test.dat)]),CallStmt(Id(ReWrite),[Id(myFile)]),CallStmt(Id(Write),[Id(myFile),ArrayCell(Id(arrayInt),IntLiteral(1))]),CallStmt(Id(Close),[Id(myFile)]),CallStmt(Id(ReSet),[Id(myFile)]),CallStmt(Id(Read),[Id(myFile),ArrayCell(Id(arrayInt),IntLiteral(2))]),CallStmt(Id(Close),[Id(myFile)]),For(Id(i)IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(Writeln),[Id(i),StringLiteral(: ),ArrayCell(ArrayCell(Id(arrayInt),IntLiteral(2)),Id(i))])]),CallStmt(Id(Readln),[])])])'
        self.assertTrue(TestAST.test(code,expect,375))


    def test_376(self):
        code = \
        """
        function can_swap(a, b: integer): boolean;
        var
        c: integer;
        begin
        if a<=b then exit(false);
        c:=a; a:=b; b:=c;
        exit(true);
        end

        procedure combsort(a: integer; n: integer);
        var
        i, g: integer;
        swapped: boolean;
        begin
        g := n;
        while (g=1) and (not swapped) do
        begin
            g := max(g * 10 div 13, 1);
            swapped := false;
            for i := 1 to n-g do
            if can_swap(a[i], a[i+g]) then
            swapped := true;
        end 
        end 
        """
        expect = 'Program([FuncDecl(Id(can_swap),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],BoolType,[VarDecl(Id(c),IntType)],[If(BinaryOp(<=,Id(a),Id(b)),[CallStmt(Id(exit),[BooleanLiteral(False)])],[]),AssignStmt(Id(c),Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),CallStmt(Id(exit),[BooleanLiteral(True)])]),FuncDecl(Id(combsort),[VarDecl(Id(a),IntType),VarDecl(Id(n),IntType)],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(g),IntType),VarDecl(Id(swapped),BoolType)],[AssignStmt(Id(g),Id(n)),While(BinaryOp(and,BinaryOp(=,Id(g),IntLiteral(1)),UnaryOp(not,Id(swapped))),[AssignStmt(Id(g),CallExpr(Id(max),[BinaryOp(div,BinaryOp(*,Id(g),IntLiteral(10)),IntLiteral(13)),IntLiteral(1)])),AssignStmt(Id(swapped),BooleanLiteral(False)),For(Id(i)IntLiteral(1),BinaryOp(-,Id(n),Id(g)),True,[If(CallExpr(Id(can_swap),[ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),BinaryOp(+,Id(i),Id(g)))]),[AssignStmt(Id(swapped),BooleanLiteral(True))],[])])])])])'
        self.assertTrue(TestAST.test(code,expect,376))


    def test_377(self):
        code = \
        """
        function maximumSum(a : array[1 .. 3] of integer) : integer;
        var lowest : integer;
            current : integer;
            i : integer;
        begin
            result := low(result);
            for i := low(a) to high(a) do
            begin
                current := a[i];
                maximize(result, current - lowest);
                minimize(lowest, current);
            end
        //    writeln("maximumSum = ", result);
        end
        """
        expect = 'Program([FuncDecl(Id(maximumSum),[VarDecl(Id(a),ArrayType(1,3,IntType))],IntType,[VarDecl(Id(lowest),IntType),VarDecl(Id(current),IntType),VarDecl(Id(i),IntType)],[AssignStmt(Id(result),CallExpr(Id(low),[Id(result)])),For(Id(i)CallExpr(Id(low),[Id(a)]),CallExpr(Id(high),[Id(a)]),True,[AssignStmt(Id(current),ArrayCell(Id(a),Id(i))),CallStmt(Id(maximize),[Id(result),BinaryOp(-,Id(current),Id(lowest))]),CallStmt(Id(minimize),[Id(lowest),Id(current)])])])])'
        self.assertTrue(TestAST.test(code,expect,377))


    def test_378(self):
        code = \
        """
        procedure main();
        var i, j, k : integer;
            answer : integer; //
        begin

            readln(n);
            answer := low(answer);

            for i := 1 to n do
            for j := 1 to n do
                read(a[i][j]);

            for i := 1 to n do
            for j := i to n do
            for k := 1 to n do
                a:=0;
            //s[i][j][k] := s[i][j-1][k] + a[j][k];

            for i := 1 to n do
            for j := i to n do
                a:=0;
            //maximize(answer, maximumSum(s[i][j][1..n]));

            writeln(answer);
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),VarDecl(Id(k),IntType),VarDecl(Id(answer),IntType)],[CallStmt(Id(readln),[Id(n)]),AssignStmt(Id(answer),CallExpr(Id(low),[Id(answer)])),For(Id(i)IntLiteral(1),Id(n),True,[For(Id(j)IntLiteral(1),Id(n),True,[CallStmt(Id(read),[ArrayCell(ArrayCell(Id(a),Id(i)),Id(j))])])]),For(Id(i)IntLiteral(1),Id(n),True,[For(Id(j)Id(i),Id(n),True,[For(Id(k)IntLiteral(1),Id(n),True,[AssignStmt(Id(a),IntLiteral(0))])])]),For(Id(i)IntLiteral(1),Id(n),True,[For(Id(j)Id(i),Id(n),True,[AssignStmt(Id(a),IntLiteral(0))])]),CallStmt(Id(writeln),[Id(answer)])])])'
        self.assertTrue(TestAST.test(code,expect,378))


    def test_379(self):
        code = \
        """
        procedure minimize(a : integer; b : integer);
        begin
            if a>b then a := b;
        end
        procedure maximize(a : integer; b : integer);
        begin
            if a<b then a := b;
        end
        """
        expect = 'Program([FuncDecl(Id(minimize),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[If(BinaryOp(>,Id(a),Id(b)),[AssignStmt(Id(a),Id(b))],[])]),FuncDecl(Id(maximize),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[If(BinaryOp(<,Id(a),Id(b)),[AssignStmt(Id(a),Id(b))],[])])])'
        self.assertTrue(TestAST.test(code,expect,379))


    def test_380(self):
        code = \
        """
        function bsearch(a : array[1 .. 2] of integer; n, key : integer) : integer;
        var ll, rr, i : integer;
        begin
            ll := 1; rr := n; i := (ll+rr) div 2;
            while (ll<>i) and (rr<>i) do
            begin
                if a[i]>=key
                then rr := i;
                else ll := i;
                i := (ll+rr) div 2;
            end
            for i := ll to rr do
            if a[i]>=key then exit(i);
            exit(0);
        end
        """
        expect = 'Program([FuncDecl(Id(bsearch),[VarDecl(Id(a),ArrayType(1,2,IntType)),VarDecl(Id(n),IntType),VarDecl(Id(key),IntType)],IntType,[VarDecl(Id(ll),IntType),VarDecl(Id(rr),IntType),VarDecl(Id(i),IntType)],[AssignStmt(Id(ll),IntLiteral(1)),AssignStmt(Id(rr),Id(n)),AssignStmt(Id(i),BinaryOp(div,BinaryOp(+,Id(ll),Id(rr)),IntLiteral(2))),While(BinaryOp(and,BinaryOp(<>,Id(ll),Id(i)),BinaryOp(<>,Id(rr),Id(i))),[If(BinaryOp(>=,ArrayCell(Id(a),Id(i)),Id(key)),[AssignStmt(Id(rr),Id(i))],[AssignStmt(Id(ll),Id(i))]),AssignStmt(Id(i),BinaryOp(div,BinaryOp(+,Id(ll),Id(rr)),IntLiteral(2)))]),For(Id(i)Id(ll),Id(rr),True,[If(BinaryOp(>=,ArrayCell(Id(a),Id(i)),Id(key)),[CallStmt(Id(exit),[Id(i)])],[])]),CallStmt(Id(exit),[IntLiteral(0)])])])'
        self.assertTrue(TestAST.test(code,expect,380))


    def test_381(self):
        code = \
        """
        procedure main();
        var a : array [0 .. 1230997] of integer;
            n, key : integer;

            i : integer;
        begin
            readln(n);
            for i := 1 to n do
            read(a[i]);

            while not seekeof do
            begin
                readln(key);
                i := bsearch(a, n, key);
                if i=0 then writeln("Not found");
                else writeln(a[i]);
            end
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(a),ArrayType(0,1230997,IntType)),VarDecl(Id(n),IntType),VarDecl(Id(key),IntType),VarDecl(Id(i),IntType)],[CallStmt(Id(readln),[Id(n)]),For(Id(i)IntLiteral(1),Id(n),True,[CallStmt(Id(read),[ArrayCell(Id(a),Id(i))])]),While(UnaryOp(not,Id(seekeof)),[CallStmt(Id(readln),[Id(key)]),AssignStmt(Id(i),CallExpr(Id(bsearch),[Id(a),Id(n),Id(key)])),If(BinaryOp(=,Id(i),IntLiteral(0)),[CallStmt(Id(writeln),[StringLiteral(Not found)])],[CallStmt(Id(writeln),[ArrayCell(Id(a),Id(i))])])])])])'
        self.assertTrue(TestAST.test(code,expect,381))


    def test_382(self):
        code = \
        """
        procedure llRotate(x : integer);
        var y : integer;
        begin
            if x + rr=NULL then exit();
            y := x + rr;
            rr := y + ll;
            if y+ ll <> NULL then y := x;
            y := x+ pp;
            if x<>root then
                if x=x + pp +  ll
                then x := y;
                else x := y;
            else root := y;
            y := x;
            x := y;
        end
        """
        expect = 'Program([FuncDecl(Id(llRotate),[VarDecl(Id(x),IntType)],VoidType(),[VarDecl(Id(y),IntType)],[If(BinaryOp(=,BinaryOp(+,Id(x),Id(rr)),Id(NULL)),[CallStmt(Id(exit),[])],[]),AssignStmt(Id(y),BinaryOp(+,Id(x),Id(rr))),AssignStmt(Id(rr),BinaryOp(+,Id(y),Id(ll))),If(BinaryOp(<>,BinaryOp(+,Id(y),Id(ll)),Id(NULL)),[AssignStmt(Id(y),Id(x))],[]),AssignStmt(Id(y),BinaryOp(+,Id(x),Id(pp))),If(BinaryOp(<>,Id(x),Id(root)),[If(BinaryOp(=,Id(x),BinaryOp(+,BinaryOp(+,Id(x),Id(pp)),Id(ll))),[AssignStmt(Id(x),Id(y))],[AssignStmt(Id(x),Id(y))])],[AssignStmt(Id(root),Id(y))]),AssignStmt(Id(y),Id(x)),AssignStmt(Id(x),Id(y))])])'
        self.assertTrue(TestAST.test(code,expect,382))


    def test_383(self):
        code = \
        """
        Function Factorial(n : Integer) : Integer;
        Var
            Result : Integer;
            i : Integer;

        Begin
            Result := n;
            If (n <= 1) Then
                Result := 1;
            Else
            For i := n-1 DownTo 1 do
                Result := Result * i; 
            Factorial := Result;
        End 
        """
        expect = 'Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType),VarDecl(Id(i),IntType)],[AssignStmt(Id(Result),Id(n)),If(BinaryOp(<=,Id(n),IntLiteral(1)),[AssignStmt(Id(Result),IntLiteral(1))],[For(Id(i)BinaryOp(-,Id(n),IntLiteral(1)),IntLiteral(1),False,[AssignStmt(Id(Result),BinaryOp(*,Id(Result),Id(i)))])]),AssignStmt(Id(Factorial),Id(Result))])])'
        self.assertTrue(TestAST.test(code,expect,383))


    def test_384(self):
        code = \
        """
        Function Factorial(n : Integer) : Integer;
        Var
            Result : Integer;

        Begin
            If n = 1 Then 
                Factorial := 1;
            Else
                Factorial := n*Factorial(n-1);
        End 
        """
        expect = 'Program([FuncDecl(Id(Factorial),[VarDecl(Id(n),IntType)],IntType,[VarDecl(Id(Result),IntType)],[If(BinaryOp(=,Id(n),IntLiteral(1)),[AssignStmt(Id(Factorial),IntLiteral(1))],[AssignStmt(Id(Factorial),BinaryOp(*,Id(n),CallExpr(Id(Factorial),[BinaryOp(-,Id(n),IntLiteral(1))])))])])])'
        self.assertTrue(TestAST.test(code,expect,384))


    def test_385(self):
        code = \
        """
        Procedure InitStack();
        Begin
            topPointer := 0;
        End
        """
        expect = 'Program([FuncDecl(Id(InitStack),[],VoidType(),[],[AssignStmt(Id(topPointer),IntLiteral(0))])])'
        self.assertTrue(TestAST.test(code,expect,385))


    def test_386(self):
        code = \
        """
        Function IsEmpty() : Boolean;
        Begin
            IsEmpty := False;
            If (topPointer = 0) Then
                IsEmpty := true;
        End
        """
        expect = 'Program([FuncDecl(Id(IsEmpty),[],BoolType,[],[AssignStmt(Id(IsEmpty),BooleanLiteral(False)),If(BinaryOp(=,Id(topPointer),IntLiteral(0)),[AssignStmt(Id(IsEmpty),BooleanLiteral(True))],[])])])'
        self.assertTrue(TestAST.test(code,expect,386))


    def test_387(self):
        code = \
        """
        Function IsFull(): Boolean;
        Begin
            IsFull := False;
            If ((topPointer + 1) = STACK_SIZE) Then
                IsFull := True;
        End
        """
        expect = 'Program([FuncDecl(Id(IsFull),[],BoolType,[],[AssignStmt(Id(IsFull),BooleanLiteral(False)),If(BinaryOp(=,BinaryOp(+,Id(topPointer),IntLiteral(1)),Id(STACK_SIZE)),[AssignStmt(Id(IsFull),BooleanLiteral(True))],[])])])'
        self.assertTrue(TestAST.test(code,expect,387))


    def test_388(self):
        code = \
        """
        Function Pop() : Integer;

        Begin
            Pop := nil;

            If not IsEmpty Then
            Begin
                Pop := myStack[topPointer];
                topPointer := topPointer - 1; 
            End
        End 
        """
        expect = 'Program([FuncDecl(Id(Pop),[],IntType,[],[AssignStmt(Id(Pop),Id(nil)),If(UnaryOp(not,Id(IsEmpty)),[AssignStmt(Id(Pop),ArrayCell(Id(myStack),Id(topPointer))),AssignStmt(Id(topPointer),BinaryOp(-,Id(topPointer),IntLiteral(1)))],[])])])'
        self.assertTrue(TestAST.test(code,expect,388))


    def test_389(self):
        code = \
        """
        Procedure Push(item : integer);
        Begin
            If not IsFull Then
            Begin
                myStack[topPointer+1] := item;
                topPointer := topPointer + 1;
            End
        End
        """
        expect = 'Program([FuncDecl(Id(Push),[VarDecl(Id(item),IntType)],VoidType(),[],[If(UnaryOp(not,Id(IsFull)),[AssignStmt(ArrayCell(Id(myStack),BinaryOp(+,Id(topPointer),IntLiteral(1))),Id(item)),AssignStmt(Id(topPointer),BinaryOp(+,Id(topPointer),IntLiteral(1)))],[])])])'
        self.assertTrue(TestAST.test(code,expect,389))


    def test_390(self):
        code = \
        """
        Function GetSize(): Integer;
        Begin
            GetSize := topPointer;
        End
        """
        expect = 'Program([FuncDecl(Id(GetSize),[],IntType,[],[AssignStmt(Id(GetSize),Id(topPointer))])])'
        self.assertTrue(TestAST.test(code,expect,390))


    def test_391(self):
        code = \
        """
        procedure DisplayMenu();
        begin
        WriteLn("Press 1: To print the area of the circle");
        WriteLn("Press 2: To print the diameter of the circle");
        WriteLn("Press q: To quit");
        Write("Enter option: ");
        end
        
        function GetRadius() : real;
        var
        radius : real;
        begin
        Write("Enter the radius: ");
        ReadLn(radius);
        GetRadius := radius;
        end
        
        procedure PrintArea();
        var
        radius, area : real;
        begin
        radius := GetRadius();
        area := PI * radius * radius;
        
        WriteLn("The area is ", area);
        end
        
        procedure PrintDiameter();
        var
        radius, diameter : real;
        begin
        radius := GetRadius();
        diameter := 2 * radius;
        
        WriteLn("The diameter is ", diameter);
        end
        
        procedure Pause();
        begin
        Write("Press enter to continue...");
        ReadLn();
        end
        """
        expect = 'Program([FuncDecl(Id(DisplayMenu),[],VoidType(),[],[CallStmt(Id(WriteLn),[StringLiteral(Press 1: To print the area of the circle)]),CallStmt(Id(WriteLn),[StringLiteral(Press 2: To print the diameter of the circle)]),CallStmt(Id(WriteLn),[StringLiteral(Press q: To quit)]),CallStmt(Id(Write),[StringLiteral(Enter option: )])]),FuncDecl(Id(GetRadius),[],FloatType,[VarDecl(Id(radius),FloatType)],[CallStmt(Id(Write),[StringLiteral(Enter the radius: )]),CallStmt(Id(ReadLn),[Id(radius)]),AssignStmt(Id(GetRadius),Id(radius))]),FuncDecl(Id(PrintArea),[],VoidType(),[VarDecl(Id(radius),FloatType),VarDecl(Id(area),FloatType)],[AssignStmt(Id(radius),CallExpr(Id(GetRadius),[])),AssignStmt(Id(area),BinaryOp(*,BinaryOp(*,Id(PI),Id(radius)),Id(radius))),CallStmt(Id(WriteLn),[StringLiteral(The area is ),Id(area)])]),FuncDecl(Id(PrintDiameter),[],VoidType(),[VarDecl(Id(radius),FloatType),VarDecl(Id(diameter),FloatType)],[AssignStmt(Id(radius),CallExpr(Id(GetRadius),[])),AssignStmt(Id(diameter),BinaryOp(*,IntLiteral(2),Id(radius))),CallStmt(Id(WriteLn),[StringLiteral(The diameter is ),Id(diameter)])]),FuncDecl(Id(Pause),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Press enter to continue...)]),CallStmt(Id(ReadLn),[])])])'
        self.assertTrue(TestAST.test(code,expect,391))


    def test_392(self):
        code = \
        """
        procedure Main();
        var
        toPrint: Integer;
        i: Integer;
        begin
        for i := 0 to 255 do
        begin
            toPrint := Char(i);
            Write(i, " ");
            
            if IsPrintable(toPrint) then
            begin
            Write(toPrint);
            end
            else
            begin
            Write(" ");
            end
            
            if ((i + 1) mod 10) = 0 then
            begin
            WriteLn();
            end
        end
        end
        """
        expect = 'Program([FuncDecl(Id(Main),[],VoidType(),[VarDecl(Id(toPrint),IntType),VarDecl(Id(i),IntType)],[For(Id(i)IntLiteral(0),IntLiteral(255),True,[AssignStmt(Id(toPrint),CallExpr(Id(Char),[Id(i)])),CallStmt(Id(Write),[Id(i),StringLiteral( )]),If(CallExpr(Id(IsPrintable),[Id(toPrint)]),[CallStmt(Id(Write),[Id(toPrint)])],[CallStmt(Id(Write),[StringLiteral( )])]),If(BinaryOp(=,BinaryOp(mod,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(10)),IntLiteral(0)),[CallStmt(Id(WriteLn),[])],[])])])])'
        self.assertTrue(TestAST.test(code,expect,392))


    def test_393(self):
        code = \
        """
        procedure SetupGraphicsWindow(title: integer);
        var
            gd, gm : integer;
        begin
        gm := vgahi;
        gd := vga;
        
        InitGraph(gd, gm, " ");
        
        if GraphResult <> grOk then
        begin
            Writeln("Graph driver ",gd," graph mode ",gm," not supported");
            Halt(1);
        end
            
        WindowsSetWindowText(GraphWindow, title);
        end
            
        //All draws the circles to the screen.
        procedure Main();
        begin
        Randomize();
        SetupGraphicsWindow("Screen Saver Sample");
            
        //You can set the colors to RGB values
        //The following code sets index 1 to (0, 255, 0) = Green
        //SetRGBPalette(1, 0, 255, 0);
                
        SetLineStyle(SolidLn, 0, ThickWidth);
        end 
        """
        expect = 'Program([FuncDecl(Id(SetupGraphicsWindow),[VarDecl(Id(title),IntType)],VoidType(),[VarDecl(Id(gd),IntType),VarDecl(Id(gm),IntType)],[AssignStmt(Id(gm),Id(vgahi)),AssignStmt(Id(gd),Id(vga)),CallStmt(Id(InitGraph),[Id(gd),Id(gm),StringLiteral( )]),If(BinaryOp(<>,Id(GraphResult),Id(grOk)),[CallStmt(Id(Writeln),[StringLiteral(Graph driver ),Id(gd),StringLiteral( graph mode ),Id(gm),StringLiteral( not supported)]),CallStmt(Id(Halt),[IntLiteral(1)])],[]),CallStmt(Id(WindowsSetWindowText),[Id(GraphWindow),Id(title)])]),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Randomize),[]),CallStmt(Id(SetupGraphicsWindow),[StringLiteral(Screen Saver Sample)]),CallStmt(Id(SetLineStyle),[Id(SolidLn),IntLiteral(0),Id(ThickWidth)])])])'
        self.assertTrue(TestAST.test(code,expect,393))


    def test_394(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,394))


    def test_395(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,395))


    def test_396(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,396))


    def test_397(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,397))


    def test_398(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,398))


    def test_399(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,399))


    def test_400(self):
        code = \
        """
        procedure main();
        begin
            pass();
        end 
        """
        expect = 'Program([FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(pass),[])])])'
        self.assertTrue(TestAST.test(code,expect,400))


















