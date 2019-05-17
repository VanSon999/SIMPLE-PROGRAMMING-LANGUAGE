import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: var i:integer;
		j,:real;
	procedure main();
	begin
	end """
        input = """
        var i:integer;
		    j,:real;
	    procedure main();
	    begin
	    end"""
        expect = "Error on line 2 col 7: :"
        self.assertTrue(TestParser.test(input,expect,301))
    def test_2(self):
        input = """var i:array [-3 .. -2] of integer;
			j,x:array [-1 .. -2] of;
		procedure main();
		begin
		end"""
        expect = "Error on line 2 col 28: ;"
        self.assertTrue(TestParser.test(input,expect,302))
    
    def test_3(self):
        input = """procedure main(a:INTEGER;b:REAL);
		begin
		end
		procedure foo();
		begin"""
        expect = "Error on line 6 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,303))

    def test_4(self):
        input = """function main(a,b:real):integer;
		begin
		end
		function foo():;
		begin
		end"""
        expect = "Error on line 4 col 16: ;"
        self.assertTrue(TestParser.test(input,expect,304))
    def test_5(self):
        input = """function main(; begin end"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,305))
    def test_var_dec_6(self):
        input = """var y : array [5 .. 6,2 .. 4] of integer ;"""
        expect = "Error on line 1 col 21: ,"
        self.assertTrue(TestParser.test(input,expect,306)) 
    def test_procedure_7(self):
        input = """procedure foo ( a : array [ 3 .. 4 ] of  integer);
        procedure goo ( x : array [ 3 .. 4 ] of  integer);
        var
        y : array [2 .. 3] of  real;
        z : array [1 .. 2] of  integer;
        begin
        foo(x);
        foo1(y)
        foo2(z) ; 
        end"""
        expect = "Error on line 9 col 8: foo2"
        self.assertTrue(TestParser.test(input,expect,307)) 
    def test_array_index_8(self):
        input = """ var y : array [ 2-3 .. 4+1 ] of real; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,308))
    def test_full_pro_9(self):
        input = """ procedure foo(d:integer; i:real);
        var d: real;
        begin
        for i := 3 to 10 do 
        d := d +2;
        break;
        end """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,309))
    def test_while_statement_10(self):
        input = """pROCEDURE foo(c: integer) ;
                   var d:real ;
                   BEGIN
                    whILe(a<=1) do beGin end
                   EnD"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,310))
    # chu y kieu a = TRUE;