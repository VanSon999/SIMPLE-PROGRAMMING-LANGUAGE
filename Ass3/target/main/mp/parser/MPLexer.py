# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u026f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\39\39\3:\3:\3;\3;\3;")
        buf.write("\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3F\3F\3G\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3N\3N\7N\u01c6\nN\f")
        buf.write("N\16N\u01c9\13N\3N\3N\3N\3N\3N\3O\3O\7O\u01d2\nO\fO\16")
        buf.write("O\u01d5\13O\3O\3O\3O\3O\3P\3P\3P\3P\7P\u01df\nP\fP\16")
        buf.write("P\u01e2\13P\3P\3P\3Q\3Q\3Q\3Q\7Q\u01ea\nQ\fQ\16Q\u01ed")
        buf.write("\13Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\7R\u01fb\nR\f")
        buf.write("R\16R\u01fe\13R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u021b\n")
        buf.write("S\3T\6T\u021e\nT\rT\16T\u021f\3U\3U\3U\6U\u0225\nU\rU")
        buf.write("\16U\u0226\5U\u0229\nU\3U\3U\6U\u022d\nU\rU\16U\u022e")
        buf.write("\5U\u0231\nU\3U\5U\u0234\nU\3U\3U\3U\5U\u0239\nU\3V\3")
        buf.write("V\5V\u023d\nV\3V\3V\3W\3W\7W\u0243\nW\fW\16W\u0246\13")
        buf.write("W\3W\3W\3W\3X\6X\u024c\nX\rX\16X\u024d\3X\3X\3Y\3Y\5Y")
        buf.write("\u0254\nY\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\7\\\u025e\n\\\f\\")
        buf.write("\16\\\u0261\13\\\3\\\3\\\3\\\3\\\3]\3]\7]\u0269\n]\f]")
        buf.write("\16]\u026c\13]\3]\3]\5\u01c7\u01d3\u01eb\2^\3\2\5\2\7")
        buf.write("\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35")
        buf.write("\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39")
        buf.write("\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23")
        buf.write("Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m\36o\37q s!u")
        buf.write("\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b")
        buf.write("-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097\63\u0099")
        buf.write("\64\u009b\65\u009d\66\u009f\67\u00a18\u00a39\u00a5\2\u00a7")
        buf.write(":\u00a9;\u00ab\2\u00ad<\u00af=\u00b1\2\u00b3\2\u00b5>")
        buf.write("\u00b7?\u00b9@\3\2!\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4")
        buf.write("\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4")
        buf.write("\2[[{{\4\2\\\\||\4\2\f\f\17\17\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\2\u027d\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\3\u00bb\3\2\2")
        buf.write("\2\5\u00bd\3\2\2\2\7\u00bf\3\2\2\2\t\u00c1\3\2\2\2\13")
        buf.write("\u00c3\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00c9")
        buf.write("\3\2\2\2\23\u00cb\3\2\2\2\25\u00cd\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00d3\3\2\2\2\35\u00d5\3\2")
        buf.write("\2\2\37\u00d7\3\2\2\2!\u00d9\3\2\2\2#\u00db\3\2\2\2%\u00dd")
        buf.write("\3\2\2\2\'\u00df\3\2\2\2)\u00e1\3\2\2\2+\u00e3\3\2\2\2")
        buf.write("-\u00e5\3\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb")
        buf.write("\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3\2\2\29\u00f5\3\2")
        buf.write("\2\2;\u00fe\3\2\2\2=\u0102\3\2\2\2?\u0105\3\2\2\2A\u010c")
        buf.write("\3\2\2\2C\u010f\3\2\2\2E\u0112\3\2\2\2G\u0117\3\2\2\2")
        buf.write("I\u011c\3\2\2\2K\u0122\3\2\2\2M\u0128\3\2\2\2O\u012c\3")
        buf.write("\2\2\2Q\u0135\3\2\2\2S\u013c\3\2\2\2U\u0146\3\2\2\2W\u014a")
        buf.write("\3\2\2\2Y\u014f\3\2\2\2[\u0155\3\2\2\2]\u015b\3\2\2\2")
        buf.write("_\u015e\3\2\2\2a\u0163\3\2\2\2c\u016b\3\2\2\2e\u0173\3")
        buf.write("\2\2\2g\u017a\3\2\2\2i\u017e\3\2\2\2k\u0182\3\2\2\2m\u0185")
        buf.write("\3\2\2\2o\u0189\3\2\2\2q\u018d\3\2\2\2s\u018f\3\2\2\2")
        buf.write("u\u0191\3\2\2\2w\u0194\3\2\2\2y\u0196\3\2\2\2{\u0198\3")
        buf.write("\2\2\2}\u019b\3\2\2\2\177\u019d\3\2\2\2\u0081\u019f\3")
        buf.write("\2\2\2\u0083\u01a3\3\2\2\2\u0085\u01a5\3\2\2\2\u0087\u01a8")
        buf.write("\3\2\2\2\u0089\u01ad\3\2\2\2\u008b\u01af\3\2\2\2\u008d")
        buf.write("\u01b1\3\2\2\2\u008f\u01b4\3\2\2\2\u0091\u01b6\3\2\2\2")
        buf.write("\u0093\u01b8\3\2\2\2\u0095\u01bb\3\2\2\2\u0097\u01bd\3")
        buf.write("\2\2\2\u0099\u01bf\3\2\2\2\u009b\u01c1\3\2\2\2\u009d\u01cf")
        buf.write("\3\2\2\2\u009f\u01da\3\2\2\2\u00a1\u01e5\3\2\2\2\u00a3")
        buf.write("\u01f7\3\2\2\2\u00a5\u021a\3\2\2\2\u00a7\u021d\3\2\2\2")
        buf.write("\u00a9\u0238\3\2\2\2\u00ab\u023a\3\2\2\2\u00ad\u0240\3")
        buf.write("\2\2\2\u00af\u024b\3\2\2\2\u00b1\u0253\3\2\2\2\u00b3\u0255")
        buf.write("\3\2\2\2\u00b5\u0258\3\2\2\2\u00b7\u025b\3\2\2\2\u00b9")
        buf.write("\u0266\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc\4\3\2\2\2\u00bd")
        buf.write("\u00be\t\3\2\2\u00be\6\3\2\2\2\u00bf\u00c0\t\4\2\2\u00c0")
        buf.write("\b\3\2\2\2\u00c1\u00c2\t\5\2\2\u00c2\n\3\2\2\2\u00c3\u00c4")
        buf.write("\t\6\2\2\u00c4\f\3\2\2\2\u00c5\u00c6\t\7\2\2\u00c6\16")
        buf.write("\3\2\2\2\u00c7\u00c8\t\b\2\2\u00c8\20\3\2\2\2\u00c9\u00ca")
        buf.write("\t\t\2\2\u00ca\22\3\2\2\2\u00cb\u00cc\t\n\2\2\u00cc\24")
        buf.write("\3\2\2\2\u00cd\u00ce\t\13\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\t\f\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\t\r\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\t\16\2\2\u00d4\34\3\2\2\2\u00d5\u00d6")
        buf.write("\t\17\2\2\u00d6\36\3\2\2\2\u00d7\u00d8\t\20\2\2\u00d8")
        buf.write(" \3\2\2\2\u00d9\u00da\t\21\2\2\u00da\"\3\2\2\2\u00db\u00dc")
        buf.write("\t\22\2\2\u00dc$\3\2\2\2\u00dd\u00de\t\23\2\2\u00de&\3")
        buf.write("\2\2\2\u00df\u00e0\t\24\2\2\u00e0(\3\2\2\2\u00e1\u00e2")
        buf.write("\t\25\2\2\u00e2*\3\2\2\2\u00e3\u00e4\t\26\2\2\u00e4,\3")
        buf.write("\2\2\2\u00e5\u00e6\t\27\2\2\u00e6.\3\2\2\2\u00e7\u00e8")
        buf.write("\t\30\2\2\u00e8\60\3\2\2\2\u00e9\u00ea\t\31\2\2\u00ea")
        buf.write("\62\3\2\2\2\u00eb\u00ec\t\32\2\2\u00ec\64\3\2\2\2\u00ed")
        buf.write("\u00ee\t\33\2\2\u00ee\66\3\2\2\2\u00ef\u00f0\5\5\3\2\u00f0")
        buf.write("\u00f1\5%\23\2\u00f1\u00f2\5\13\6\2\u00f2\u00f3\5\3\2")
        buf.write("\2\u00f3\u00f4\5\27\f\2\u00f48\3\2\2\2\u00f5\u00f6\5\7")
        buf.write("\4\2\u00f6\u00f7\5\37\20\2\u00f7\u00f8\5\35\17\2\u00f8")
        buf.write("\u00f9\5)\25\2\u00f9\u00fa\5\23\n\2\u00fa\u00fb\5\35\17")
        buf.write("\2\u00fb\u00fc\5+\26\2\u00fc\u00fd\5\13\6\2\u00fd:\3\2")
        buf.write("\2\2\u00fe\u00ff\5\r\7\2\u00ff\u0100\5\37\20\2\u0100\u0101")
        buf.write("\5%\23\2\u0101<\3\2\2\2\u0102\u0103\5)\25\2\u0103\u0104")
        buf.write("\5\37\20\2\u0104>\3\2\2\2\u0105\u0106\5\t\5\2\u0106\u0107")
        buf.write("\5\37\20\2\u0107\u0108\5/\30\2\u0108\u0109\5\35\17\2\u0109")
        buf.write("\u010a\5)\25\2\u010a\u010b\5\37\20\2\u010b@\3\2\2\2\u010c")
        buf.write("\u010d\5\t\5\2\u010d\u010e\5\37\20\2\u010eB\3\2\2\2\u010f")
        buf.write("\u0110\5\23\n\2\u0110\u0111\5\r\7\2\u0111D\3\2\2\2\u0112")
        buf.write("\u0113\5)\25\2\u0113\u0114\5\21\t\2\u0114\u0115\5\13\6")
        buf.write("\2\u0115\u0116\5\35\17\2\u0116F\3\2\2\2\u0117\u0118\5")
        buf.write("\13\6\2\u0118\u0119\5\31\r\2\u0119\u011a\5\'\24\2\u011a")
        buf.write("\u011b\5\13\6\2\u011bH\3\2\2\2\u011c\u011d\5/\30\2\u011d")
        buf.write("\u011e\5\21\t\2\u011e\u011f\5\23\n\2\u011f\u0120\5\31")
        buf.write("\r\2\u0120\u0121\5\13\6\2\u0121J\3\2\2\2\u0122\u0123\5")
        buf.write("\5\3\2\u0123\u0124\5\13\6\2\u0124\u0125\5\17\b\2\u0125")
        buf.write("\u0126\5\23\n\2\u0126\u0127\5\35\17\2\u0127L\3\2\2\2\u0128")
        buf.write("\u0129\5\13\6\2\u0129\u012a\5\35\17\2\u012a\u012b\5\t")
        buf.write("\5\2\u012bN\3\2\2\2\u012c\u012d\5\r\7\2\u012d\u012e\5")
        buf.write("+\26\2\u012e\u012f\5\35\17\2\u012f\u0130\5\7\4\2\u0130")
        buf.write("\u0131\5)\25\2\u0131\u0132\5\23\n\2\u0132\u0133\5\37\20")
        buf.write("\2\u0133\u0134\5\35\17\2\u0134P\3\2\2\2\u0135\u0136\5")
        buf.write("%\23\2\u0136\u0137\5\13\6\2\u0137\u0138\5)\25\2\u0138")
        buf.write("\u0139\5+\26\2\u0139\u013a\5%\23\2\u013a\u013b\5\35\17")
        buf.write("\2\u013bR\3\2\2\2\u013c\u013d\5!\21\2\u013d\u013e\5%\23")
        buf.write("\2\u013e\u013f\5\37\20\2\u013f\u0140\5\7\4\2\u0140\u0141")
        buf.write("\5\13\6\2\u0141\u0142\5\t\5\2\u0142\u0143\5+\26\2\u0143")
        buf.write("\u0144\5%\23\2\u0144\u0145\5\13\6\2\u0145T\3\2\2\2\u0146")
        buf.write("\u0147\5-\27\2\u0147\u0148\5\3\2\2\u0148\u0149\5%\23\2")
        buf.write("\u0149V\3\2\2\2\u014a\u014b\5)\25\2\u014b\u014c\5%\23")
        buf.write("\2\u014c\u014d\5+\26\2\u014d\u014e\5\13\6\2\u014eX\3\2")
        buf.write("\2\2\u014f\u0150\5\r\7\2\u0150\u0151\5\3\2\2\u0151\u0152")
        buf.write("\5\31\r\2\u0152\u0153\5\'\24\2\u0153\u0154\5\13\6\2\u0154")
        buf.write("Z\3\2\2\2\u0155\u0156\5\3\2\2\u0156\u0157\5%\23\2\u0157")
        buf.write("\u0158\5%\23\2\u0158\u0159\5\3\2\2\u0159\u015a\5\63\32")
        buf.write("\2\u015a\\\3\2\2\2\u015b\u015c\5\37\20\2\u015c\u015d\5")
        buf.write("\r\7\2\u015d^\3\2\2\2\u015e\u015f\5%\23\2\u015f\u0160")
        buf.write("\5\13\6\2\u0160\u0161\5\3\2\2\u0161\u0162\5\31\r\2\u0162")
        buf.write("`\3\2\2\2\u0163\u0164\5\5\3\2\u0164\u0165\5\37\20\2\u0165")
        buf.write("\u0166\5\37\20\2\u0166\u0167\5\31\r\2\u0167\u0168\5\13")
        buf.write("\6\2\u0168\u0169\5\3\2\2\u0169\u016a\5\35\17\2\u016ab")
        buf.write("\3\2\2\2\u016b\u016c\5\23\n\2\u016c\u016d\5\35\17\2\u016d")
        buf.write("\u016e\5)\25\2\u016e\u016f\5\13\6\2\u016f\u0170\5\17\b")
        buf.write("\2\u0170\u0171\5\13\6\2\u0171\u0172\5%\23\2\u0172d\3\2")
        buf.write("\2\2\u0173\u0174\5\'\24\2\u0174\u0175\5)\25\2\u0175\u0176")
        buf.write("\5%\23\2\u0176\u0177\5\23\n\2\u0177\u0178\5\35\17\2\u0178")
        buf.write("\u0179\5\17\b\2\u0179f\3\2\2\2\u017a\u017b\5\35\17\2\u017b")
        buf.write("\u017c\5\37\20\2\u017c\u017d\5)\25\2\u017dh\3\2\2\2\u017e")
        buf.write("\u017f\5\3\2\2\u017f\u0180\5\35\17\2\u0180\u0181\5\t\5")
        buf.write("\2\u0181j\3\2\2\2\u0182\u0183\5\37\20\2\u0183\u0184\5")
        buf.write("%\23\2\u0184l\3\2\2\2\u0185\u0186\5\t\5\2\u0186\u0187")
        buf.write("\5\23\n\2\u0187\u0188\5-\27\2\u0188n\3\2\2\2\u0189\u018a")
        buf.write("\5\33\16\2\u018a\u018b\5\37\20\2\u018b\u018c\5\t\5\2\u018c")
        buf.write("p\3\2\2\2\u018d\u018e\7-\2\2\u018er\3\2\2\2\u018f\u0190")
        buf.write("\7,\2\2\u0190t\3\2\2\2\u0191\u0192\7>\2\2\u0192\u0193")
        buf.write("\7@\2\2\u0193v\3\2\2\2\u0194\u0195\7>\2\2\u0195x\3\2\2")
        buf.write("\2\u0196\u0197\7?\2\2\u0197z\3\2\2\2\u0198\u0199\5w<\2")
        buf.write("\u0199\u019a\5y=\2\u019a|\3\2\2\2\u019b\u019c\7/\2\2\u019c")
        buf.write("~\3\2\2\2\u019d\u019e\7\61\2\2\u019e\u0080\3\2\2\2\u019f")
        buf.write("\u01a0\5\33\16\2\u01a0\u01a1\5\37\20\2\u01a1\u01a2\5\t")
        buf.write("\5\2\u01a2\u0082\3\2\2\2\u01a3\u01a4\7@\2\2\u01a4\u0084")
        buf.write("\3\2\2\2\u01a5\u01a6\5\u0083B\2\u01a6\u01a7\5y=\2\u01a7")
        buf.write("\u0086\3\2\2\2\u01a8\u01a9\5/\30\2\u01a9\u01aa\5\23\n")
        buf.write("\2\u01aa\u01ab\5)\25\2\u01ab\u01ac\5\21\t\2\u01ac\u0088")
        buf.write("\3\2\2\2\u01ad\u01ae\7]\2\2\u01ae\u008a\3\2\2\2\u01af")
        buf.write("\u01b0\7_\2\2\u01b0\u008c\3\2\2\2\u01b1\u01b2\7\60\2\2")
        buf.write("\u01b2\u01b3\7\60\2\2\u01b3\u008e\3\2\2\2\u01b4\u01b5")
        buf.write("\7.\2\2\u01b5\u0090\3\2\2\2\u01b6\u01b7\7<\2\2\u01b7\u0092")
        buf.write("\3\2\2\2\u01b8\u01b9\7<\2\2\u01b9\u01ba\7?\2\2\u01ba\u0094")
        buf.write("\3\2\2\2\u01bb\u01bc\7*\2\2\u01bc\u0096\3\2\2\2\u01bd")
        buf.write("\u01be\7+\2\2\u01be\u0098\3\2\2\2\u01bf\u01c0\7=\2\2\u01c0")
        buf.write("\u009a\3\2\2\2\u01c1\u01c2\7*\2\2\u01c2\u01c3\7,\2\2\u01c3")
        buf.write("\u01c7\3\2\2\2\u01c4\u01c6\13\2\2\2\u01c5\u01c4\3\2\2")
        buf.write("\2\u01c6\u01c9\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca")
        buf.write("\u01cb\7,\2\2\u01cb\u01cc\7+\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01ce\bN\2\2\u01ce\u009c\3\2\2\2\u01cf\u01d3\7}\2\2\u01d0")
        buf.write("\u01d2\13\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5\3\2\2")
        buf.write("\2\u01d3\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7\177\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01d9\bO\2\2\u01d9\u009e\3\2\2\2")
        buf.write("\u01da\u01db\7\61\2\2\u01db\u01dc\7\61\2\2\u01dc\u01e0")
        buf.write("\3\2\2\2\u01dd\u01df\n\34\2\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\b")
        buf.write("P\2\2\u01e4\u00a0\3\2\2\2\u01e5\u01e6\7$\2\2\u01e6\u01e7")
        buf.write("\7$\2\2\u01e7\u01eb\3\2\2\2\u01e8\u01ea\13\2\2\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb\3")
        buf.write("\2\2\2\u01ee\u01ef\7$\2\2\u01ef\u01f0\7\u0080\2\2\u01f0")
        buf.write("\u01f1\7$\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\7$\2\2\u01f3")
        buf.write("\u01f4\7$\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\bQ\2\2\u01f6")
        buf.write("\u00a2\3\2\2\2\u01f7\u01fc\5\u00a5S\2\u01f8\u01fb\5\u00a5")
        buf.write("S\2\u01f9\u01fb\5\u00a7T\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u00a4\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01ff\u021b\5\3\2\2\u0200\u021b\5\5\3\2\u0201\u021b\5")
        buf.write("\7\4\2\u0202\u021b\5\t\5\2\u0203\u021b\5\13\6\2\u0204")
        buf.write("\u021b\5\r\7\2\u0205\u021b\5\17\b\2\u0206\u021b\5\21\t")
        buf.write("\2\u0207\u021b\5\23\n\2\u0208\u021b\5\25\13\2\u0209\u021b")
        buf.write("\5\27\f\2\u020a\u021b\5\31\r\2\u020b\u021b\5\33\16\2\u020c")
        buf.write("\u021b\5\35\17\2\u020d\u021b\5\37\20\2\u020e\u021b\5!")
        buf.write("\21\2\u020f\u021b\5#\22\2\u0210\u021b\5%\23\2\u0211\u021b")
        buf.write("\5\'\24\2\u0212\u021b\5)\25\2\u0213\u021b\5+\26\2\u0214")
        buf.write("\u021b\5-\27\2\u0215\u021b\5/\30\2\u0216\u021b\5\61\31")
        buf.write("\2\u0217\u021b\5\63\32\2\u0218\u021b\5\65\33\2\u0219\u021b")
        buf.write("\7a\2\2\u021a\u01ff\3\2\2\2\u021a\u0200\3\2\2\2\u021a")
        buf.write("\u0201\3\2\2\2\u021a\u0202\3\2\2\2\u021a\u0203\3\2\2\2")
        buf.write("\u021a\u0204\3\2\2\2\u021a\u0205\3\2\2\2\u021a\u0206\3")
        buf.write("\2\2\2\u021a\u0207\3\2\2\2\u021a\u0208\3\2\2\2\u021a\u0209")
        buf.write("\3\2\2\2\u021a\u020a\3\2\2\2\u021a\u020b\3\2\2\2\u021a")
        buf.write("\u020c\3\2\2\2\u021a\u020d\3\2\2\2\u021a\u020e\3\2\2\2")
        buf.write("\u021a\u020f\3\2\2\2\u021a\u0210\3\2\2\2\u021a\u0211\3")
        buf.write("\2\2\2\u021a\u0212\3\2\2\2\u021a\u0213\3\2\2\2\u021a\u0214")
        buf.write("\3\2\2\2\u021a\u0215\3\2\2\2\u021a\u0216\3\2\2\2\u021a")
        buf.write("\u0217\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2")
        buf.write("\u021b\u00a6\3\2\2\2\u021c\u021e\t\35\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u00a8\3\2\2\2\u0221\u0222\5\u00a7")
        buf.write("T\2\u0222\u0228\7\60\2\2\u0223\u0225\t\35\2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0224\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229\u0231\3\2\2\2\u022a\u022c\7")
        buf.write("\60\2\2\u022b\u022d\t\35\2\2\u022c\u022b\3\2\2\2\u022d")
        buf.write("\u022e\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u0231\3\2\2\2\u0230\u0221\3\2\2\2\u0230\u022a\3")
        buf.write("\2\2\2\u0231\u0233\3\2\2\2\u0232\u0234\5\u00abV\2\u0233")
        buf.write("\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0239\3\2\2\2")
        buf.write("\u0235\u0236\5\u00a7T\2\u0236\u0237\5\u00abV\2\u0237\u0239")
        buf.write("\3\2\2\2\u0238\u0230\3\2\2\2\u0238\u0235\3\2\2\2\u0239")
        buf.write("\u00aa\3\2\2\2\u023a\u023c\5\13\6\2\u023b\u023d\5}?\2")
        buf.write("\u023c\u023b\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\3")
        buf.write("\2\2\2\u023e\u023f\5\u00a7T\2\u023f\u00ac\3\2\2\2\u0240")
        buf.write("\u0244\7$\2\2\u0241\u0243\5\u00b1Y\2\u0242\u0241\3\2\2")
        buf.write("\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245")
        buf.write("\3\2\2\2\u0245\u0247\3\2\2\2\u0246\u0244\3\2\2\2\u0247")
        buf.write("\u0248\7$\2\2\u0248\u0249\bW\3\2\u0249\u00ae\3\2\2\2\u024a")
        buf.write("\u024c\t\36\2\2\u024b\u024a\3\2\2\2\u024c\u024d\3\2\2")
        buf.write("\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f")
        buf.write("\3\2\2\2\u024f\u0250\bX\2\2\u0250\u00b0\3\2\2\2\u0251")
        buf.write("\u0254\n\37\2\2\u0252\u0254\5\u00b3Z\2\u0253\u0251\3\2")
        buf.write("\2\2\u0253\u0252\3\2\2\2\u0254\u00b2\3\2\2\2\u0255\u0256")
        buf.write("\7^\2\2\u0256\u0257\t \2\2\u0257\u00b4\3\2\2\2\u0258\u0259")
        buf.write("\13\2\2\2\u0259\u025a\b[\4\2\u025a\u00b6\3\2\2\2\u025b")
        buf.write("\u025f\7$\2\2\u025c\u025e\5\u00b1Y\2\u025d\u025c\3\2\2")
        buf.write("\2\u025e\u0261\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f\3\2\2\2\u0262")
        buf.write("\u0263\7^\2\2\u0263\u0264\n \2\2\u0264\u0265\b\\\5\2\u0265")
        buf.write("\u00b8\3\2\2\2\u0266\u026a\7$\2\2\u0267\u0269\5\u00b1")
        buf.write("Y\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268")
        buf.write("\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026d\3\2\2\2\u026c")
        buf.write("\u026a\3\2\2\2\u026d\u026e\b]\6\2\u026e\u00ba\3\2\2\2")
        buf.write("\27\2\u01c7\u01d3\u01e0\u01eb\u01fa\u01fc\u021a\u021f")
        buf.write("\u0226\u0228\u022e\u0230\u0233\u0238\u023c\u0244\u024d")
        buf.write("\u0253\u025f\u026a\7\b\2\2\3W\2\3[\3\3\\\4\3]\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    WHILE = 10
    BEGIN = 11
    END = 12
    FUNCTION = 13
    RETURN = 14
    PROCEDURE = 15
    VAR = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    OF = 20
    REAL = 21
    BOOLEAN = 22
    INTEGER = 23
    STRING = 24
    NOT = 25
    AND = 26
    OR = 27
    DIV = 28
    MOD = 29
    ADD = 30
    MUL = 31
    NOT_EQUAD = 32
    LESS_THAN = 33
    EQUAL = 34
    LESS_THAN_EQUAL = 35
    SUB = 36
    DIVISION = 37
    MODULUS = 38
    GREATER_THAN = 39
    GREATER_THAN_EQUAL = 40
    WITH = 41
    LSB = 42
    RSB = 43
    D_DOT = 44
    COMMA = 45
    COLON = 46
    ASSIGN = 47
    LB = 48
    RB = 49
    SEMI = 50
    COMMENT_1 = 51
    COMMENT_2 = 52
    COMMENT_3 = 53
    COMMENT_4 = 54
    IDENTIFIER = 55
    INTEGER_TYPE = 56
    REAL_TYPE = 57
    STRINGLIT = 58
    WS = 59
    ERROR_CHAR = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'='", "'-'", "'/'", "'>'", "'['", 
            "']'", "'..'", "','", "':'", "':='", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "WHILE", "BEGIN", "END", "FUNCTION", "RETURN", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADD", "MUL", "NOT_EQUAD", 
            "LESS_THAN", "EQUAL", "LESS_THAN_EQUAL", "SUB", "DIVISION", 
            "MODULUS", "GREATER_THAN", "GREATER_THAN_EQUAL", "WITH", "LSB", 
            "RSB", "D_DOT", "COMMA", "COLON", "ASSIGN", "LB", "RB", "SEMI", 
            "COMMENT_1", "COMMENT_2", "COMMENT_3", "COMMENT_4", "IDENTIFIER", 
            "INTEGER_TYPE", "REAL_TYPE", "STRINGLIT", "WS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "WHILE", "BEGIN", 
                  "END", "FUNCTION", "RETURN", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADD", "MUL", 
                  "NOT_EQUAD", "LESS_THAN", "EQUAL", "LESS_THAN_EQUAL", 
                  "SUB", "DIVISION", "MODULUS", "GREATER_THAN", "GREATER_THAN_EQUAL", 
                  "WITH", "LSB", "RSB", "D_DOT", "COMMA", "COLON", "ASSIGN", 
                  "LB", "RB", "SEMI", "COMMENT_1", "COMMENT_2", "COMMENT_3", 
                  "COMMENT_4", "IDENTIFIER", "CHARACTER", "INTEGER_TYPE", 
                  "REAL_TYPE", "EXPONENT", "STRINGLIT", "WS", "STRING_S", 
                  "ESC", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[85] = self.STRINGLIT_action 
            actions[89] = self.ERROR_CHAR_action 
            actions[90] = self.ILLEGAL_ESCAPE_action 
            actions[91] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        self.text = self.text[1:-1]
                    
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                        raise ErrorToken(self.text) 
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                       raise IllegalEscape(self.text[1:])
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                            raise UncloseString(self.text[1:])
                    
     


