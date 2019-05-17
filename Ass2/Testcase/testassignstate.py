def test_70_assign_stm_with_expression_NOT(self):
        input = """
        function foo(): integer;
        begin
            x := not y and z;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(and,UnaryOp(not,Id(y)),Id(z)))])])')
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71_assign_stm_with_functioncall_without_param(self):
        input = """
        function foo(): integer;
        begin
            x := foo() + 1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(1)))])])')
        self.assertTrue(TestAST.test(input,expect,371))

    def test_72_assign_stm_with_functioncall_with_one_param(self):
        input = """
        function foo(): integer;
        begin
            x := foo(123) + 1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(+,CallExpr(Id(foo),[IntLiteral(123)]),IntLiteral(1)))])])')
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73_assign_stm_with_functioncall_with_many_param(self):
        input = """
        function foo(): integer;
        begin
            x := range(10,0,-2) + 1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(+,CallExpr(Id(range),[IntLiteral(10),IntLiteral(0),UnaryOp(-,IntLiteral(2))]),IntLiteral(1)))])])')
        self.assertTrue(TestAST.test(input,expect,373))

    def test_74_assign_stm_MP_document_example(self):
        input = """
        function foo(): integer;
        begin
            a := b[10] := foo()[3] := x := 1+1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(+,IntLiteral(1),IntLiteral(1))),AssignStmt(ArrayCell(CallExpr(Id(foo),[]),IntLiteral(3)),Id(x)),AssignStmt(ArrayCell(Id(b),IntLiteral(10)),ArrayCell(CallExpr(Id(foo),[]),IntLiteral(3))),AssignStmt(Id(a),ArrayCell(Id(b),IntLiteral(10)))])])')
        self.assertTrue(TestAST.test(input,expect,374))

    def test_75_function_declaration_MP_document_example(self):
        input = """
        function foo(a,b: integer; c: real): array [1 .. 2] of integer;
        var x,y: real;
        begin
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)],ArrayType(1,2,IntType),[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType)],[])])')
        self.assertTrue(TestAST.test(input,expect,375))

    def test_76_compound_stm_with_assignment_stm(self):
        input = """
        function foo(): integer;
        begin
            x := 1;
            begin
                x:=2;
                x:=3;
            end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),IntLiteral(1)),AssignStmt(Id(x),IntLiteral(2)),AssignStmt(Id(x),IntLiteral(3))])])')
        self.assertTrue(TestAST.test(input,expect,376))

    def test_78_for_stm_with_one_statement(self):
        input = """
        function foo(): integer;
        begin
            for x := 1 TO 5 DO a:=x;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(x)IntLiteral(1),IntLiteral(5),True,[AssignStmt(Id(a),Id(x))])])])')
        self.assertTrue(TestAST.test(input,expect,378))

    def test_79_for_stm_with_many_statement(self):
        input = """
        function foo(): integer;
        begin
            for x := 1 TO 5 DO
                begin
                    a := x + 1;
                    b := x - 1;
                end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(x)IntLiteral(1),IntLiteral(5),True,[AssignStmt(Id(a),BinaryOp(+,Id(x),IntLiteral(1))),AssignStmt(Id(b),BinaryOp(-,Id(x),IntLiteral(1)))])])])')
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80_for_stm_with_downto_option(self):
        input = """
        function foo(): integer;
        begin
            for x := 1 downTO 5 DO
                begin
                    a := x + 1;
                    b := x - 1;
                end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(x)IntLiteral(1),IntLiteral(5),False,[AssignStmt(Id(a),BinaryOp(+,Id(x),IntLiteral(1))),AssignStmt(Id(b),BinaryOp(-,Id(x),IntLiteral(1)))])])])')
        self.assertTrue(TestAST.test(input,expect,380))

    def test_81_for_stm_with_complex_expression(self):
        input = """
        function foo(): integer;
        begin
            for x := x*2 + 1 TO foo()[3] DO
                b := a := x;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(x)BinaryOp(+,BinaryOp(*,Id(x),IntLiteral(2)),IntLiteral(1)),ArrayCell(CallExpr(Id(foo),[]),IntLiteral(3)),True,[AssignStmt(Id(a),Id(x)),AssignStmt(Id(b),Id(a))])])])')
        self.assertTrue(TestAST.test(input,expect,381))

    def test_82_function_with_assign_and_for_stm(self):
        input = """
        function foo(): integer;
        begin
            x := 0;
            for i := 1 TO 10 DO
                x := x + i;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),IntLiteral(0)),For(Id(i)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(x),BinaryOp(+,Id(x),Id(i)))])])])')
        self.assertTrue(TestAST.test(input,expect,382))

    def test_83_function_with_while_stm_one_stm(self):
        input = """
        function foo(): integer;
        begin
            while x DO x:= false;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[While(Id(x),[AssignStmt(Id(x),BooleanLiteral(False))])])])')
        self.assertTrue(TestAST.test(input,expect,383))

    def test_84_function_with_while_stm_many_stm(self):
        input = """
        function foo(): integer;
        begin
            while x DO
            begin
                x:= false;
                z:= y;
            end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[While(Id(x),[AssignStmt(Id(x),BooleanLiteral(False)),AssignStmt(Id(z),Id(y))])])])')
        self.assertTrue(TestAST.test(input,expect,384))

    def test_85_function_with_while_stm_inside_for(self):
        input = """
        function foo(): integer;
        begin
            for i := 1 to 2 do
                while i = 1 do
                    i := 0;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)IntLiteral(1),IntLiteral(2),True,[While(BinaryOp(=,Id(i),IntLiteral(1)),[AssignStmt(Id(i),IntLiteral(0))])])])])')
        self.assertTrue(TestAST.test(input,expect,385))

    def test_86_break_stm_in_function_decl(self):
        input = """
        function foo(): integer;
        begin
            x := 0;
            breaK;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),IntLiteral(0)),Break])])')
        self.assertTrue(TestAST.test(input,expect,386))

    def test_87_break_stm_inside_while_stm(self):
        input = """
        function foo(): integer;
        begin
            while x >= 0 DO
            Begin
                x := 0;
                breaK;
            End
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(>=,Id(x),IntLiteral(0)),[AssignStmt(Id(x),IntLiteral(0)),Break])])])')
        self.assertTrue(TestAST.test(input,expect,387))

    def test_88_if_stm_without_else(self):
        input = """
        function foo(): integer;
        begin
            if a <> 2
            then a:= 2;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(<>,Id(a),IntLiteral(2)),[AssignStmt(Id(a),IntLiteral(2))],[])])])')
        self.assertTrue(TestAST.test(input,expect,388))

    def test_89_if_stm_with_else_stm(self):
        input = """
        function foo(): integer;
        begin
            if a <> 2
            then a:= 2;
            else a := a+1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(<>,Id(a),IntLiteral(2)),[AssignStmt(Id(a),IntLiteral(2))],[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])')
        self.assertTrue(TestAST.test(input,expect,389))

    def test_90_if_stm_with_else_stm_complex_expr(self):
        input = """
        function foo(): integer;
        begin
            if a or foo(b,c)
            then a:= 2;
            else a := a+1;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(or,Id(a),CallExpr(Id(foo),[Id(b),Id(c)])),[AssignStmt(Id(a),IntLiteral(2))],[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])])])')
        self.assertTrue(TestAST.test(input,expect,90))

    def test_91_if_stm_with_else_stm_compound_stm(self):
        input = """
        function foo(): integer;
        begin
            if true
            then
            begin
                b := 1;
                a := b;
            end
            else
            begin
                b := 2;
                a := b;
            end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BooleanLiteral(True),[AssignStmt(Id(b),IntLiteral(1)),AssignStmt(Id(a),Id(b))],[AssignStmt(Id(b),IntLiteral(2)),AssignStmt(Id(a),Id(b))])])])')
        self.assertTrue(TestAST.test(input,expect,391))

    def test_92_if_stm_with_else_stm_if_stm_nest(self):
        input = """
        function foo(): integer;
        begin
            if true
            then
                if false
                then a:=b;
            else
            a:=c;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BooleanLiteral(True),[If(BooleanLiteral(False),[AssignStmt(Id(a),Id(b))],[AssignStmt(Id(a),Id(c))])],[])])])')
        self.assertTrue(TestAST.test(input,expect,392))

    def test_93_if_stm_without_else_stm_if_stm_nest(self):
        input = """
        function foo(): integer;
        begin
            if true
            then
                begin
                if false
                then a:=b;
                end
            else
            a:=c;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[If(BooleanLiteral(True),[If(BooleanLiteral(False),[AssignStmt(Id(a),Id(b))],[])],[AssignStmt(Id(a),Id(c))])])])')
        self.assertTrue(TestAST.test(input,expect,393))

    def test_94_test_function_return_stm(self):
        input = """
        function foo(): integer;
        begin
            a := 1;
            return a;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(a),IntLiteral(1)),Return(Some(Id(a)))])])')
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95_test_procedure_return_stm(self):
        input = """
        function foo(): integer;
        begin
            a := 1;
            return;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(a),IntLiteral(1)),Return(None)])])')
        self.assertTrue(TestAST.test(input,expect,395))

    def test_96_test_with_stm_one_vardecl_one_stm(self):
        input = """
        function foo(): integer;
        begin
            with c: integer; do c := 5;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(c),IntType)],[AssignStmt(Id(c),IntLiteral(5))])])])')
        self.assertTrue(TestAST.test(input,expect,396))

    def test_97_test_with_stm_many_vardecl_one_stm(self):
        input = """
        function foo(): integer;
        begin
            with a,b:integer; c: array [1 .. 2] of real; do
                d := c[a] + b;
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),ArrayType(1,2,FloatType))],[AssignStmt(Id(d),BinaryOp(+,ArrayCell(Id(c),Id(a)),Id(b)))])])])')
        self.assertTrue(TestAST.test(input,expect,397))

    def test_98_test_with_stm_many_vardecl_compound_stm(self):
        input = """
        function foo(): integer;
        begin
            with a,b:integer; c: array [1 .. 2] of real; do
                begin
                    a := 1;
                    b := 2;
                    d := c[a] + c[b];
                end
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),ArrayType(1,2,FloatType))],[AssignStmt(Id(a),IntLiteral(1)),AssignStmt(Id(b),IntLiteral(2)),AssignStmt(Id(d),BinaryOp(+,ArrayCell(Id(c),Id(a)),ArrayCell(Id(c),Id(b))))])])])')
        self.assertTrue(TestAST.test(input,expect,398))

    def test_99_test_call_stm_without_param(self):
        input = """
        function foo(): integer;
        begin
            foo();
            goo();
        end
        """
        expect = str('Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[]),CallStmt(Id(goo),[])])])')
        self.assertTrue(TestAST.test(input,expect,399))