import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
    def test_comment_1(self):
        self.assertTrue(TestLexer.test("{abc}","<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))
    def test_comment_4(self):
        self.assertTrue(TestLexer.test("//ascw_12","<EOF>",105))
    def test_comment_5(self):
        self.assertTrue(TestLexer.test("(*asrcsd*)","<EOF>",103))
    def test_ESC_6(self):
        self.assertTrue(TestLexer.test("\dsdwds123","Error Token \\",106))
    def test_string_7(self):
        self.assertTrue(TestLexer.test(""" "kamer \b" """, "kamer \b,<EOF>", 107))
    def test_ESC_8(self):
        self.assertTrue(TestLexer.test("\"aa\\\\\"", "aa\\\\,<EOF>", 108)) 
    def test_ESC_9(self):
        self.assertTrue(TestLexer.test('"cv\\\\b"',"cv\\\\b,<EOF>",109))
    def test_ESC_10(self):
        self.assertTrue(TestLexer.test("c\\d", "c,Error Token \\", 110))
    def test_ESC_11(self):
        self.assertTrue(TestLexer.test("adf\bsdw", "adf,Error Token \b", 111))
    def test_ESC_12(self):
        self.assertTrue(TestLexer.test("\"dsf", "Unclosed String: dsf", 112))
    def test_ESC_13(self):
        self.assertTrue(TestLexer.test("d \tev\besr", "d,ev,Error Token \b", 113))
    def test_ESC_14(self):
        self.assertTrue(TestLexer.test("dwec\ttvs\f", "dwec,tvs,Error Token \f", 114))
    def test_ESC_15(self):
        self.assertTrue(TestLexer.test("\rqssfe\n", "qssfe,<EOF>", 115))
    def test_ESC_16(self):
        self.assertTrue(TestLexer.test("qwf\rwds\b\t", "qwf,wds,Error Token \b", 116))
    def test_comment_17(self):
        self.assertTrue(TestLexer.test("{//}", "<EOF>", 117))
    def test_comment_18(self):
        self.assertTrue(TestLexer.test("//\n", "<EOF>", 118))
    def test_comment_19(self):
        self.assertTrue(TestLexer.test("(*//}", "(,*,<EOF>", 119))
    def test_comment_20(self):
        self.assertTrue(TestLexer.test("{asdsd}/*)", "/,*,),<EOF>", 120))
    def test_comment_21(self):
        self.assertTrue(TestLexer.test("//(asf){tdf}qc10", "<EOF>", 121))
    def test_comment_22(self):
        self.assertTrue(TestLexer.test("{reff85}_asq//sf", "_asq,<EOF>", 122))
    def test_comment_23(self):
        self.assertTrue(TestLexer.test("(*ads85sd*)", "<EOF>", 123))
    def test_comment_24(self):
        self.assertTrue(TestLexer.test("(*{sddhsjc}adh3*)dsbdw{235}", "dsbdw,<EOF>", 124))
    def test_comment_25(self):
        self.assertTrue(TestLexer.test("{235}dsd//uiasd(*sdwdv*)jkcw", "dsd,<EOF>", 125))
    def test_identifier_26(self):
        self.assertTrue(TestLexer.test("__sd_sdhn123", "__sd_sdhn123,<EOF>", 126))
    def test_identifier_27(self):
        self.assertTrue(TestLexer.test("wck123_wcj", "wck123_wcj,<EOF>", 127))
    def test_identifier_28(self):
        self.assertTrue(TestLexer.test("___158___hdk_", "___158___hdk_,<EOF>", 128))
    def test_identifier_29(self):
        self.assertTrue(TestLexer.test("dwwc_89_qc", "dwwc_89_qc,<EOF>", 129))
    def test_identifier_30(self):
        self.assertTrue(TestLexer.test("rfw_86_dr____saq56", "rfw_86_dr____saq56,<EOF>", 130))
    def test_identifier_31(self):
        self.assertTrue(TestLexer.test("____999/9999_______sasq_", "____999,/,9999,_______sasq_,<EOF>", 131))
    def test_identifier_32(self):
        self.assertTrue(TestLexer.test("_s_c_w_9_w_", "_s_c_w_9_w_,<EOF>", 132))
    def test_identifier_33(self):
        self.assertTrue(TestLexer.test("w8e*v5e6_e", "w8e,*,v5e6_e,<EOF>", 133))
    def test_identifier_34(self):
        self.assertTrue(TestLexer.test("_8_9_10\_", "_8_9_10,Error Token \\", 134))
    def test_string_35(self):
        self.assertTrue(TestLexer.test("\"986asdw_\"", "986asdw_,<EOF>", 135))
    def test_string_36(self):
        self.assertTrue(TestLexer.test("\dcdw\bdwdc\"", "Error Token \\", 136))
    def test_string_37(self):
        self.assertTrue(TestLexer.test("\"sdwc\t wdwr\"", "sdwc	 wdwr,<EOF>", 137))
    def test_string_38(self):
        self.assertTrue(TestLexer.test("\"538_dwdj\n sqsf\"", "Unclosed String: 538_dwdj", 138))
    def test_string_39(self):
        self.assertTrue(TestLexer.test("\"aaa_bbb\f swd\"", "aaa_bbb swd,<EOF>", 139))
    def test_string_40(self):
        self.assertTrue(TestLexer.test("\"852_qc\b \wdws\"", "Illegal Escape In String: 852_qc\b \w", 140))
    def test_string_41(self):
        self.assertTrue(TestLexer.test("\"ercs_qsd'sq'\"", "ercs_qsd'sq',<EOF>", 141))
    def test_string_42(self):
        self.assertTrue(TestLexer.test("\"tec_qxw86\|sq\rsdc\"", "Illegal Escape In String: tec_qxw86\|", 142))
    def test_string_43(self):
        self.assertTrue(TestLexer.test(""" "html23x \n" """, "Unclosed String: html23x ", 143))
    def test_string_44(self):
        self.assertTrue(TestLexer.test(""" "htm\rl23x " """, "Unclosed String: htm", 144))
    def test_string_45(self):
        self.assertTrue(TestLexer.test("\"""dwde_c\fvw ""\"", "dwde_cvw ,<EOF>", 145))
    def test_string_46(self):
        self.assertTrue(TestLexer.test("\"te'\"r_534\"", "te',r_534,Error Token \"", 146))
    def test_operator_47(self):
        self.assertTrue(TestLexer.test("+-=a=b=e", "+,-,=,a,=,b,=,e,<EOF>", 147))
    def test_operator_48(self):
        self.assertTrue(TestLexer.test("a+c=b-d>(e MOD t)", "a,+,c,=,b,-,d,>,(,e,MOD,t,),<EOF>", 148))
    def test_operator_49(self):
        self.assertTrue(TestLexer.test("atr <> trc With res / has", "atr,<>,trc,With,res,/,has,<EOF>", 149))
    def test_operator_50(self):
        self.assertTrue(TestLexer.test("(rec - e*wc) MOD t >= (er / tr)", "(,rec,-,e,*,wc,),MOD,t,>=,(,er,/,tr,),<EOF>", 150))
    def test_operator_51(self):
        self.assertTrue(TestLexer.test("(RET >= trc) = (ec MOD tr) <= hd", "(,RET,>=,trc,),=,(,ec,MOD,tr,),<=,hd,<EOF>", 151))
    def test_operator_52(self):
        self.assertTrue(TestLexer.test("WiTh th >< <> k MoD tmt - rts", "WiTh,th,>,<,<>,k,MoD,tmt,-,rts,<EOF>", 152))
    def test_operator_53(self):
        self.assertTrue(TestLexer.test("+-*/mOd > wITh <> <= < > =", "+,-,*,/,mOd,>,wITh,<>,<=,<,>,=,<EOF>", 153))
    def test_operator_54(self):
        self.assertTrue(TestLexer.test("tmn MOD tnt - exs >= tem WIth -- == ++ ** /", "tmn,MOD,tnt,-,exs,>=,tem,WIth,-,-,=,=,+,+,*,*,/,<EOF>", 154))
    def test_operator_55(self):
        self.assertTrue(TestLexer.test("a+b -c /d moD WitH <> ><", "a,+,b,-,c,/,d,moD,WitH,<>,>,<,<EOF>", 155))
    def test_operator_56(self):
        self.assertTrue(TestLexer.test("r >< t <> c >=w <=t = e Mod x", "r,>,<,t,<>,c,>=,w,<=,t,=,e,Mod,x,<EOF>", 156))
    def test_operators_57(self):
        self.assertTrue(TestLexer.test("MoD WiTh dcw + - */ <> ><", "MoD,WiTh,dcw,+,-,*,/,<>,>,<,<EOF>", 157))
    def test_separators_58(self):
        self.assertTrue(TestLexer.test("[a + b] = c+d", "[,a,+,b,],=,c,+,d,<EOF>", 158))
    def test_separators_59(self):
        self.assertTrue(TestLexer.test("] , [ ..", "],,,[,..,<EOF>", 159))
    def test_separators_60(self):
        self.assertTrue(TestLexer.test("[swe + dc,f] : [89/36]", "[,swe,+,dc,,,f,],:,[,89,/,36,],<EOF>", 160))
    def test_separators_61(self):
        self.assertTrue(TestLexer.test("as + ed , ed - dw : [8 .. 9]", "as,+,ed,,,ed,-,dw,:,[,8,..,9,],<EOF>", 161))
    def test_separators_62(self):
        self.assertTrue(TestLexer.test("]:[ trs .. trf", "],:,[,trs,..,trf,<EOF>", 162))
    def test_separators_63(self):
        self.assertTrue(TestLexer.test("[MOD a+ c] : [With c..d]", "[,MOD,a,+,c,],:,[,With,c,..,d,],<EOF>", 163))
    def test_separators_64(self):
        self.assertTrue(TestLexer.test("[a >= c] .. [b <> d] : end", "[,a,>=,c,],..,[,b,<>,d,],:,end,<EOF>", 164))
    def test_separators_65(self):
        self.assertTrue(TestLexer.test("[c:d]:[c,d]:[c..d]", "[,c,:,d,],:,[,c,,,d,],:,[,c,..,d,],<EOF>", 165))
    def test_separators_66(self):
        self.assertTrue(TestLexer.test(",,,,,[[[]]]]::::", ",,,,,,,,,,[,[,[,],],],],:,:,:,:,<EOF>", 166))
    def test_separators_67(self):
        self.assertTrue(TestLexer.test("]]]],],]],],]]],]][,[[,[[[:[[:[[", "],],],],,,],,,],],,,],,,],],],,,],],[,,,[,[,,,[,[,[,:,[,[,:,[,[,<EOF>", 167))
    def test_keyworks_68(self):
        self.assertTrue(TestLexer.test("BreAK a,", "BreAK,a,,,<EOF>", 168))
    def test_keyworks_69(self):
        self.assertTrue(TestLexer.test("CONtinuE + tO", "CONtinuE,+,tO,<EOF>", 169))
    def test_keyworks_70(self):
        self.assertTrue(TestLexer.test("iF ThEn ElSe : BeGin : EnD", "iF,ThEn,ElSe,:,BeGin,:,EnD,<EOF>", 170))
    def test_keyworks_71(self):
        self.assertTrue(TestLexer.test("ArrAy OF InteGeR And _integer", "ArrAy,OF,InteGeR,And,_integer,<EOF>", 171))
    def test_keyworks_72(self):
        self.assertTrue(TestLexer.test("BeGIN ReAl Or BooLeAN anD StrINg Not ArraY eNd", "BeGIN,ReAl,Or,BooLeAN,anD,StrINg,Not,ArraY,eNd,<EOF>", 172))
    def test_keyworks_73(self):
        self.assertTrue(TestLexer.test("DiV MoD WhILe (Down tO| To)", "DiV,MoD,WhILe,(,Down,tO,Error Token |", 173))
    def test_keyworks_74(self):
        self.assertTrue(TestLexer.test("VaR x: InteGer, Real, Array [TRue\|FaLse]", "VaR,x,:,InteGer,,,Real,,,Array,[,TRue,Error Token \\", 174))
    def test_keyworks_75(self):
        self.assertTrue(TestLexer.test("WhiLe x = y Do BeGin x: REal End", "WhiLe,x,=,y,Do,BeGin,x,:,REal,End,<EOF>", 175))
    def test_keyworks_76(self):
        self.assertTrue(TestLexer.test("ArraY [1 .. 5]: BooLean", "ArraY,[,1,..,5,],:,BooLean,<EOF>", 176))
    def test_keyworks_77(self):
        self.assertTrue(TestLexer.test("FunCtion Not ProCeDure", "FunCtion,Not,ProCeDure,<EOF>", 177))
    def test_comment_78(self):
        '''test if the comment part is skipped'''
        self.assertTrue(TestLexer.test('''//This line is skipped\n This line is not skipped {But this part is skipped} (*And also this part**)''',"This,line,is,not,skipped,<EOF>",178))
    def test_str2_79(self):
        self.assertTrue(TestLexer.test(r'"NH"6\\"51Q"84q4"j175\\ersdfewf68"j450""\\7""1\\\\S""""587""AGJ""\\4D"4"P02R1vQ1\\"""06u6"2"W""8"5nc"\\"s0j"K"843\\\\',"NH,6,Error Token \\",179))
    def test_id1_80(self):
        self.assertTrue(TestLexer.test('1  wdsjkcaskfw 43K  S5v600 M0   1kQ  88  3  P 3 5g8C0   7714b3 l i _k_  q  686V1_1_8 d _6 5_8  7 G08H',"1,wdsjkcaskfw,43,K,S5v600,M0,1,kQ,88,3,P,3,5,g8C0,7714,b3,l,i,_k_,q,686,V1_1_8,d,_6,5,_8,7,G08H,<EOF>",180))
    def test_float_81(self):
        self.assertTrue(TestLexer.test("-1E87","-1E87,<EOF>",181))
    def test_float_82(self):
        self.assertTrue(TestLexer.test("2. .00 00.e-00 5.00E-010 130.10e10 01.10 100E4","2.,.00,00.e-00,5.00E-010,130.10e10,01.10,100E4,<EOF>",182))
    def test_error_token_83(self):
        self.assertTrue(TestLexer.test(";stk @",";,stk,Error Token @",183))
    def test_index_84(self):
        self.assertTrue(TestLexer.test("Hi[1]","Hi,[,1,],<EOF>",184))
    def test_function_index_85(self):
        self.assertTrue(TestLexer.test("foo(2)[4+x]","foo,(,2,),[,4,+,x,],<EOF>",185))
    def test_string_86(self):
        self.assertTrue(TestLexer.test("\"program123 (*abc*) language\"","program123 (*abc*) language,<EOF>",186))
    def test_float_87(self):
        self.assertTrue(TestLexer.test("-1.E-4","-1.E-4,<EOF>",187))
    def test_int_88(self):
        self.assertTrue(TestLexer.test("+-456456","+,-456456,<EOF>",188))
    def test_id_89(self):
        self.assertTrue(TestLexer.test("0ONE_5_THEE4_FIV","0,ONE_5_THEE4_FIV,<EOF>",189))
    def test_op_division_90(self):
        self.assertTrue(TestLexer.test("4/3","4,/,3,<EOF>",190)) 
    def test_separators_91(self):
        self.assertTrue(TestLexer.test("...","..,Error Token .",191))
    def test_float1_92(self):
        self.assertTrue(TestLexer.test("3...6","3.,..,6,<EOF>",192))
    def test_float_93(self):
        self.assertTrue(TestLexer.test("e-2","e-2,<EOF>",193))
    def test_illegal_escape_94(self):
        self.assertTrue(TestLexer.test("\"aA\thh\\a\rb\n\fdfdsf\"","Illegal Escape In String: aA	hh\\a",194))
    def test_assign_95(self):
        self.assertTrue(TestLexer.test("c := b [9] := foo()[4] := x := 2;","c,:=,b,[,9,],:=,foo,(,),[,4,],:=,x,:=,2,;,<EOF>",195))
    def test_brack_96(self):
        self.assertTrue(TestLexer.test("[]();:..,","[,],(,),;,:,..,,,<EOF>",196))
    def test_int_97(self):
        self.assertTrue(TestLexer.test("789a123","789,a123,<EOF>",197))
    def test_procedure_main_98(self):
        self.assertTrue(TestLexer.test("procedure main ();","procedure,main,(,),;,<EOF>",198))
    def test_block_cmt99(self):
        self.assertTrue(TestLexer.test("{ //=+-*/skip}","<EOF>",199))
    def test_id_100(self):
        self.assertTrue(TestLexer.test("123_RH568","123,_RH568,<EOF>",200))
    
    