# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0253\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\39\39\3:\3:\3;\3;\3;")
        buf.write("\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3F\3F\3G\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3N\3N\7N\u01c4\nN\f")
        buf.write("N\16N\u01c7\13N\3N\3N\3N\3N\3N\3O\3O\7O\u01d0\nO\fO\16")
        buf.write("O\u01d3\13O\3O\3O\3O\3O\3P\3P\3P\3P\7P\u01dd\nP\fP\16")
        buf.write("P\u01e0\13P\3P\3P\3Q\3Q\3Q\7Q\u01e7\nQ\fQ\16Q\u01ea\13")
        buf.write("Q\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3R\3R\3R\5R\u0207\nR\3S\5S\u020a\n")
        buf.write("S\3S\6S\u020d\nS\rS\16S\u020e\3T\3T\3T\5T\u0214\nT\3T")
        buf.write("\3T\5T\u0218\nT\3T\5T\u021b\nT\3T\3T\3T\5T\u0220\nT\3")
        buf.write("U\3U\3U\3V\3V\7V\u0227\nV\fV\16V\u022a\13V\3V\3V\3V\3")
        buf.write("W\6W\u0230\nW\rW\16W\u0231\3W\3W\3X\3X\5X\u0238\nX\3Y")
        buf.write("\3Y\3Y\3Z\3Z\3Z\3[\3[\7[\u0242\n[\f[\16[\u0245\13[\3[")
        buf.write("\3[\3[\3[\3\\\3\\\7\\\u024d\n\\\f\\\16\\\u0250\13\\\3")
        buf.write("\\\3\\\4\u01c5\u01d1\2]\3\2\5\2\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2")
        buf.write(")\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\n")
        buf.write("G\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30")
        buf.write("c\31e\32g\33i\34k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081")
        buf.write("(\u0083)\u0085*\u0087+\u0089,\u008b-\u008d.\u008f/\u0091")
        buf.write("\60\u0093\61\u0095\62\u0097\63\u0099\64\u009b\65\u009d")
        buf.write("\66\u009f\67\u00a18\u00a3\2\u00a59\u00a7:\u00a9\2\u00ab")
        buf.write(";\u00ad<\u00af\2\u00b1\2\u00b3=\u00b5>\u00b7?\3\2!\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f")
        buf.write("\17\17\3\2\62;\5\2\13\f\17\17\"\"\6\2\f\f\17\17$$^^\n")
        buf.write("\2$$))^^ddhhppttvv\2\u025e\2\67\3\2\2\2\29\3\2\2\2\2;")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\3\u00b9\3\2\2\2\5\u00bb\3\2\2\2\7\u00bd\3\2\2")
        buf.write("\2\t\u00bf\3\2\2\2\13\u00c1\3\2\2\2\r\u00c3\3\2\2\2\17")
        buf.write("\u00c5\3\2\2\2\21\u00c7\3\2\2\2\23\u00c9\3\2\2\2\25\u00cb")
        buf.write("\3\2\2\2\27\u00cd\3\2\2\2\31\u00cf\3\2\2\2\33\u00d1\3")
        buf.write("\2\2\2\35\u00d3\3\2\2\2\37\u00d5\3\2\2\2!\u00d7\3\2\2")
        buf.write("\2#\u00d9\3\2\2\2%\u00db\3\2\2\2\'\u00dd\3\2\2\2)\u00df")
        buf.write("\3\2\2\2+\u00e1\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3\2\2\2")
        buf.write("\61\u00e7\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67")
        buf.write("\u00ed\3\2\2\29\u00f3\3\2\2\2;\u00fc\3\2\2\2=\u0100\3")
        buf.write("\2\2\2?\u0103\3\2\2\2A\u010a\3\2\2\2C\u010d\3\2\2\2E\u0110")
        buf.write("\3\2\2\2G\u0115\3\2\2\2I\u011a\3\2\2\2K\u0120\3\2\2\2")
        buf.write("M\u0126\3\2\2\2O\u012a\3\2\2\2Q\u0133\3\2\2\2S\u013a\3")
        buf.write("\2\2\2U\u0144\3\2\2\2W\u0148\3\2\2\2Y\u014d\3\2\2\2[\u0153")
        buf.write("\3\2\2\2]\u0159\3\2\2\2_\u015c\3\2\2\2a\u0161\3\2\2\2")
        buf.write("c\u0169\3\2\2\2e\u0171\3\2\2\2g\u0178\3\2\2\2i\u017c\3")
        buf.write("\2\2\2k\u0180\3\2\2\2m\u0183\3\2\2\2o\u0187\3\2\2\2q\u018b")
        buf.write("\3\2\2\2s\u018d\3\2\2\2u\u018f\3\2\2\2w\u0192\3\2\2\2")
        buf.write("y\u0194\3\2\2\2{\u0196\3\2\2\2}\u0199\3\2\2\2\177\u019b")
        buf.write("\3\2\2\2\u0081\u019d\3\2\2\2\u0083\u01a1\3\2\2\2\u0085")
        buf.write("\u01a3\3\2\2\2\u0087\u01a6\3\2\2\2\u0089\u01ab\3\2\2\2")
        buf.write("\u008b\u01ad\3\2\2\2\u008d\u01af\3\2\2\2\u008f\u01b2\3")
        buf.write("\2\2\2\u0091\u01b4\3\2\2\2\u0093\u01b6\3\2\2\2\u0095\u01b9")
        buf.write("\3\2\2\2\u0097\u01bb\3\2\2\2\u0099\u01bd\3\2\2\2\u009b")
        buf.write("\u01bf\3\2\2\2\u009d\u01cd\3\2\2\2\u009f\u01d8\3\2\2\2")
        buf.write("\u00a1\u01e3\3\2\2\2\u00a3\u0206\3\2\2\2\u00a5\u0209\3")
        buf.write("\2\2\2\u00a7\u021f\3\2\2\2\u00a9\u0221\3\2\2\2\u00ab\u0224")
        buf.write("\3\2\2\2\u00ad\u022f\3\2\2\2\u00af\u0237\3\2\2\2\u00b1")
        buf.write("\u0239\3\2\2\2\u00b3\u023c\3\2\2\2\u00b5\u023f\3\2\2\2")
        buf.write("\u00b7\u024a\3\2\2\2\u00b9\u00ba\t\2\2\2\u00ba\4\3\2\2")
        buf.write("\2\u00bb\u00bc\t\3\2\2\u00bc\6\3\2\2\2\u00bd\u00be\t\4")
        buf.write("\2\2\u00be\b\3\2\2\2\u00bf\u00c0\t\5\2\2\u00c0\n\3\2\2")
        buf.write("\2\u00c1\u00c2\t\6\2\2\u00c2\f\3\2\2\2\u00c3\u00c4\t\7")
        buf.write("\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\t\b\2\2\u00c6\20\3\2")
        buf.write("\2\2\u00c7\u00c8\t\t\2\2\u00c8\22\3\2\2\2\u00c9\u00ca")
        buf.write("\t\n\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\t\13\2\2\u00cc\26")
        buf.write("\3\2\2\2\u00cd\u00ce\t\f\2\2\u00ce\30\3\2\2\2\u00cf\u00d0")
        buf.write("\t\r\2\2\u00d0\32\3\2\2\2\u00d1\u00d2\t\16\2\2\u00d2\34")
        buf.write("\3\2\2\2\u00d3\u00d4\t\17\2\2\u00d4\36\3\2\2\2\u00d5\u00d6")
        buf.write("\t\20\2\2\u00d6 \3\2\2\2\u00d7\u00d8\t\21\2\2\u00d8\"")
        buf.write("\3\2\2\2\u00d9\u00da\t\22\2\2\u00da$\3\2\2\2\u00db\u00dc")
        buf.write("\t\23\2\2\u00dc&\3\2\2\2\u00dd\u00de\t\24\2\2\u00de(\3")
        buf.write("\2\2\2\u00df\u00e0\t\25\2\2\u00e0*\3\2\2\2\u00e1\u00e2")
        buf.write("\t\26\2\2\u00e2,\3\2\2\2\u00e3\u00e4\t\27\2\2\u00e4.\3")
        buf.write("\2\2\2\u00e5\u00e6\t\30\2\2\u00e6\60\3\2\2\2\u00e7\u00e8")
        buf.write("\t\31\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\t\32\2\2\u00ea")
        buf.write("\64\3\2\2\2\u00eb\u00ec\t\33\2\2\u00ec\66\3\2\2\2\u00ed")
        buf.write("\u00ee\5\5\3\2\u00ee\u00ef\5%\23\2\u00ef\u00f0\5\13\6")
        buf.write("\2\u00f0\u00f1\5\3\2\2\u00f1\u00f2\5\27\f\2\u00f28\3\2")
        buf.write("\2\2\u00f3\u00f4\5\7\4\2\u00f4\u00f5\5\37\20\2\u00f5\u00f6")
        buf.write("\5\35\17\2\u00f6\u00f7\5)\25\2\u00f7\u00f8\5\23\n\2\u00f8")
        buf.write("\u00f9\5\35\17\2\u00f9\u00fa\5+\26\2\u00fa\u00fb\5\13")
        buf.write("\6\2\u00fb:\3\2\2\2\u00fc\u00fd\5\r\7\2\u00fd\u00fe\5")
        buf.write("\37\20\2\u00fe\u00ff\5%\23\2\u00ff<\3\2\2\2\u0100\u0101")
        buf.write("\5)\25\2\u0101\u0102\5\37\20\2\u0102>\3\2\2\2\u0103\u0104")
        buf.write("\5\t\5\2\u0104\u0105\5\37\20\2\u0105\u0106\5/\30\2\u0106")
        buf.write("\u0107\5\35\17\2\u0107\u0108\5)\25\2\u0108\u0109\5\37")
        buf.write("\20\2\u0109@\3\2\2\2\u010a\u010b\5\t\5\2\u010b\u010c\5")
        buf.write("\37\20\2\u010cB\3\2\2\2\u010d\u010e\5\23\n\2\u010e\u010f")
        buf.write("\5\r\7\2\u010fD\3\2\2\2\u0110\u0111\5)\25\2\u0111\u0112")
        buf.write("\5\21\t\2\u0112\u0113\5\13\6\2\u0113\u0114\5\35\17\2\u0114")
        buf.write("F\3\2\2\2\u0115\u0116\5\13\6\2\u0116\u0117\5\31\r\2\u0117")
        buf.write("\u0118\5\'\24\2\u0118\u0119\5\13\6\2\u0119H\3\2\2\2\u011a")
        buf.write("\u011b\5/\30\2\u011b\u011c\5\21\t\2\u011c\u011d\5\23\n")
        buf.write("\2\u011d\u011e\5\31\r\2\u011e\u011f\5\13\6\2\u011fJ\3")
        buf.write("\2\2\2\u0120\u0121\5\5\3\2\u0121\u0122\5\13\6\2\u0122")
        buf.write("\u0123\5\17\b\2\u0123\u0124\5\23\n\2\u0124\u0125\5\35")
        buf.write("\17\2\u0125L\3\2\2\2\u0126\u0127\5\13\6\2\u0127\u0128")
        buf.write("\5\35\17\2\u0128\u0129\5\t\5\2\u0129N\3\2\2\2\u012a\u012b")
        buf.write("\5\r\7\2\u012b\u012c\5+\26\2\u012c\u012d\5\35\17\2\u012d")
        buf.write("\u012e\5\7\4\2\u012e\u012f\5)\25\2\u012f\u0130\5\23\n")
        buf.write("\2\u0130\u0131\5\37\20\2\u0131\u0132\5\35\17\2\u0132P")
        buf.write("\3\2\2\2\u0133\u0134\5%\23\2\u0134\u0135\5\13\6\2\u0135")
        buf.write("\u0136\5)\25\2\u0136\u0137\5+\26\2\u0137\u0138\5%\23\2")
        buf.write("\u0138\u0139\5\35\17\2\u0139R\3\2\2\2\u013a\u013b\5!\21")
        buf.write("\2\u013b\u013c\5%\23\2\u013c\u013d\5\37\20\2\u013d\u013e")
        buf.write("\5\7\4\2\u013e\u013f\5\13\6\2\u013f\u0140\5\t\5\2\u0140")
        buf.write("\u0141\5+\26\2\u0141\u0142\5%\23\2\u0142\u0143\5\13\6")
        buf.write("\2\u0143T\3\2\2\2\u0144\u0145\5-\27\2\u0145\u0146\5\3")
        buf.write("\2\2\u0146\u0147\5%\23\2\u0147V\3\2\2\2\u0148\u0149\5")
        buf.write(")\25\2\u0149\u014a\5%\23\2\u014a\u014b\5+\26\2\u014b\u014c")
        buf.write("\5\13\6\2\u014cX\3\2\2\2\u014d\u014e\5\r\7\2\u014e\u014f")
        buf.write("\5\3\2\2\u014f\u0150\5\31\r\2\u0150\u0151\5\'\24\2\u0151")
        buf.write("\u0152\5\13\6\2\u0152Z\3\2\2\2\u0153\u0154\5\3\2\2\u0154")
        buf.write("\u0155\5%\23\2\u0155\u0156\5%\23\2\u0156\u0157\5\3\2\2")
        buf.write("\u0157\u0158\5\63\32\2\u0158\\\3\2\2\2\u0159\u015a\5\37")
        buf.write("\20\2\u015a\u015b\5\r\7\2\u015b^\3\2\2\2\u015c\u015d\5")
        buf.write("%\23\2\u015d\u015e\5\13\6\2\u015e\u015f\5\3\2\2\u015f")
        buf.write("\u0160\5\31\r\2\u0160`\3\2\2\2\u0161\u0162\5\5\3\2\u0162")
        buf.write("\u0163\5\37\20\2\u0163\u0164\5\37\20\2\u0164\u0165\5\31")
        buf.write("\r\2\u0165\u0166\5\13\6\2\u0166\u0167\5\3\2\2\u0167\u0168")
        buf.write("\5\35\17\2\u0168b\3\2\2\2\u0169\u016a\5\23\n\2\u016a\u016b")
        buf.write("\5\35\17\2\u016b\u016c\5)\25\2\u016c\u016d\5\13\6\2\u016d")
        buf.write("\u016e\5\17\b\2\u016e\u016f\5\13\6\2\u016f\u0170\5%\23")
        buf.write("\2\u0170d\3\2\2\2\u0171\u0172\5\'\24\2\u0172\u0173\5)")
        buf.write("\25\2\u0173\u0174\5%\23\2\u0174\u0175\5\23\n\2\u0175\u0176")
        buf.write("\5\35\17\2\u0176\u0177\5\17\b\2\u0177f\3\2\2\2\u0178\u0179")
        buf.write("\5\35\17\2\u0179\u017a\5\37\20\2\u017a\u017b\5)\25\2\u017b")
        buf.write("h\3\2\2\2\u017c\u017d\5\3\2\2\u017d\u017e\5\35\17\2\u017e")
        buf.write("\u017f\5\t\5\2\u017fj\3\2\2\2\u0180\u0181\5\37\20\2\u0181")
        buf.write("\u0182\5%\23\2\u0182l\3\2\2\2\u0183\u0184\5\t\5\2\u0184")
        buf.write("\u0185\5\23\n\2\u0185\u0186\5-\27\2\u0186n\3\2\2\2\u0187")
        buf.write("\u0188\5\33\16\2\u0188\u0189\5\37\20\2\u0189\u018a\5\t")
        buf.write("\5\2\u018ap\3\2\2\2\u018b\u018c\7-\2\2\u018cr\3\2\2\2")
        buf.write("\u018d\u018e\7,\2\2\u018et\3\2\2\2\u018f\u0190\7>\2\2")
        buf.write("\u0190\u0191\7@\2\2\u0191v\3\2\2\2\u0192\u0193\7>\2\2")
        buf.write("\u0193x\3\2\2\2\u0194\u0195\7?\2\2\u0195z\3\2\2\2\u0196")
        buf.write("\u0197\5w<\2\u0197\u0198\5y=\2\u0198|\3\2\2\2\u0199\u019a")
        buf.write("\7/\2\2\u019a~\3\2\2\2\u019b\u019c\7\61\2\2\u019c\u0080")
        buf.write("\3\2\2\2\u019d\u019e\5\33\16\2\u019e\u019f\5\37\20\2\u019f")
        buf.write("\u01a0\5\t\5\2\u01a0\u0082\3\2\2\2\u01a1\u01a2\7@\2\2")
        buf.write("\u01a2\u0084\3\2\2\2\u01a3\u01a4\5\u0083B\2\u01a4\u01a5")
        buf.write("\5y=\2\u01a5\u0086\3\2\2\2\u01a6\u01a7\5/\30\2\u01a7\u01a8")
        buf.write("\5\23\n\2\u01a8\u01a9\5)\25\2\u01a9\u01aa\5\21\t\2\u01aa")
        buf.write("\u0088\3\2\2\2\u01ab\u01ac\7]\2\2\u01ac\u008a\3\2\2\2")
        buf.write("\u01ad\u01ae\7_\2\2\u01ae\u008c\3\2\2\2\u01af\u01b0\7")
        buf.write("\60\2\2\u01b0\u01b1\7\60\2\2\u01b1\u008e\3\2\2\2\u01b2")
        buf.write("\u01b3\7.\2\2\u01b3\u0090\3\2\2\2\u01b4\u01b5\7<\2\2\u01b5")
        buf.write("\u0092\3\2\2\2\u01b6\u01b7\7<\2\2\u01b7\u01b8\7?\2\2\u01b8")
        buf.write("\u0094\3\2\2\2\u01b9\u01ba\7*\2\2\u01ba\u0096\3\2\2\2")
        buf.write("\u01bb\u01bc\7+\2\2\u01bc\u0098\3\2\2\2\u01bd\u01be\7")
        buf.write("=\2\2\u01be\u009a\3\2\2\2\u01bf\u01c0\7*\2\2\u01c0\u01c1")
        buf.write("\7,\2\2\u01c1\u01c5\3\2\2\2\u01c2\u01c4\13\2\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c8\u01c9\7,\2\2\u01c9\u01ca\7+\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01cc\bN\2\2\u01cc\u009c\3\2\2\2\u01cd")
        buf.write("\u01d1\7}\2\2\u01ce\u01d0\13\2\2\2\u01cf\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d3\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d5")
        buf.write("\7\177\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\bO\2\2\u01d7")
        buf.write("\u009e\3\2\2\2\u01d8\u01d9\7\61\2\2\u01d9\u01da\7\61\2")
        buf.write("\2\u01da\u01de\3\2\2\2\u01db\u01dd\n\34\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e1\u01e2\bP\2\2\u01e2\u00a0\3\2\2\2\u01e3\u01e8\5")
        buf.write("\u00a3R\2\u01e4\u01e7\5\u00a3R\2\u01e5\u01e7\5\u00a5S")
        buf.write("\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u00a2\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u0207\5\3\2\2")
        buf.write("\u01ec\u0207\5\5\3\2\u01ed\u0207\5\7\4\2\u01ee\u0207\5")
        buf.write("\t\5\2\u01ef\u0207\5\13\6\2\u01f0\u0207\5\r\7\2\u01f1")
        buf.write("\u0207\5\17\b\2\u01f2\u0207\5\21\t\2\u01f3\u0207\5\23")
        buf.write("\n\2\u01f4\u0207\5\25\13\2\u01f5\u0207\5\27\f\2\u01f6")
        buf.write("\u0207\5\31\r\2\u01f7\u0207\5\33\16\2\u01f8\u0207\5\35")
        buf.write("\17\2\u01f9\u0207\5\37\20\2\u01fa\u0207\5!\21\2\u01fb")
        buf.write("\u0207\5#\22\2\u01fc\u0207\5%\23\2\u01fd\u0207\5\'\24")
        buf.write("\2\u01fe\u0207\5)\25\2\u01ff\u0207\5+\26\2\u0200\u0207")
        buf.write("\5-\27\2\u0201\u0207\5/\30\2\u0202\u0207\5\61\31\2\u0203")
        buf.write("\u0207\5\63\32\2\u0204\u0207\5\65\33\2\u0205\u0207\7a")
        buf.write("\2\2\u0206\u01eb\3\2\2\2\u0206\u01ec\3\2\2\2\u0206\u01ed")
        buf.write("\3\2\2\2\u0206\u01ee\3\2\2\2\u0206\u01ef\3\2\2\2\u0206")
        buf.write("\u01f0\3\2\2\2\u0206\u01f1\3\2\2\2\u0206\u01f2\3\2\2\2")
        buf.write("\u0206\u01f3\3\2\2\2\u0206\u01f4\3\2\2\2\u0206\u01f5\3")
        buf.write("\2\2\2\u0206\u01f6\3\2\2\2\u0206\u01f7\3\2\2\2\u0206\u01f8")
        buf.write("\3\2\2\2\u0206\u01f9\3\2\2\2\u0206\u01fa\3\2\2\2\u0206")
        buf.write("\u01fb\3\2\2\2\u0206\u01fc\3\2\2\2\u0206\u01fd\3\2\2\2")
        buf.write("\u0206\u01fe\3\2\2\2\u0206\u01ff\3\2\2\2\u0206\u0200\3")
        buf.write("\2\2\2\u0206\u0201\3\2\2\2\u0206\u0202\3\2\2\2\u0206\u0203")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0205\3\2\2\2\u0207")
        buf.write("\u00a4\3\2\2\2\u0208\u020a\7/\2\2\u0209\u0208\3\2\2\2")
        buf.write("\u0209\u020a\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u020d\t")
        buf.write("\35\2\2\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u00a6\3\2\2\2")
        buf.write("\u0210\u0211\5\u00a5S\2\u0211\u0213\7\60\2\2\u0212\u0214")
        buf.write("\5\u00a5S\2\u0213\u0212\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0218\3\2\2\2\u0215\u0216\7\60\2\2\u0216\u0218\5\u00a5")
        buf.write("S\2\u0217\u0210\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u021b\5\u00a9U\2\u021a\u0219\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u0220\3\2\2\2\u021c\u021d\5\u00a5")
        buf.write("S\2\u021d\u021e\5\u00a9U\2\u021e\u0220\3\2\2\2\u021f\u0217")
        buf.write("\3\2\2\2\u021f\u021c\3\2\2\2\u0220\u00a8\3\2\2\2\u0221")
        buf.write("\u0222\5\13\6\2\u0222\u0223\5\u00a5S\2\u0223\u00aa\3\2")
        buf.write("\2\2\u0224\u0228\7$\2\2\u0225\u0227\5\u00afX\2\u0226\u0225")
        buf.write("\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022b\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022b\u022c\7$\2\2\u022c\u022d\bV\3\2\u022d\u00ac\3\2")
        buf.write("\2\2\u022e\u0230\t\36\2\2\u022f\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233\u0234\bW\2\2\u0234\u00ae\3\2\2\2")
        buf.write("\u0235\u0238\n\37\2\2\u0236\u0238\5\u00b1Y\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u00b0\3\2\2\2\u0239")
        buf.write("\u023a\7^\2\2\u023a\u023b\t \2\2\u023b\u00b2\3\2\2\2\u023c")
        buf.write("\u023d\13\2\2\2\u023d\u023e\bZ\4\2\u023e\u00b4\3\2\2\2")
        buf.write("\u023f\u0243\7$\2\2\u0240\u0242\5\u00afX\2\u0241\u0240")
        buf.write("\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243")
        buf.write("\u0244\3\2\2\2\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0246\u0247\7^\2\2\u0247\u0248\n \2\2\u0248\u0249\b[")
        buf.write("\5\2\u0249\u00b6\3\2\2\2\u024a\u024e\7$\2\2\u024b\u024d")
        buf.write("\5\u00afX\2\u024c\u024b\3\2\2\2\u024d\u0250\3\2\2\2\u024e")
        buf.write("\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0251\3\2\2\2")
        buf.write("\u0250\u024e\3\2\2\2\u0251\u0252\b\\\6\2\u0252\u00b8\3")
        buf.write("\2\2\2\24\2\u01c5\u01d1\u01de\u01e6\u01e8\u0206\u0209")
        buf.write("\u020e\u0213\u0217\u021a\u021f\u0228\u0231\u0237\u0243")
        buf.write("\u024e\7\b\2\2\3V\2\3Z\3\3[\4\3\\\5")
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
    IDENTIFIER = 54
    INTEGER_TYPE = 55
    REAL_TYPE = 56
    STRINGLIT = 57
    WS = 58
    ERROR_CHAR = 59
    ILLEGAL_ESCAPE = 60
    UNCLOSE_STRING = 61

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
            "COMMENT_1", "COMMENT_2", "COMMENT_3", "IDENTIFIER", "INTEGER_TYPE", 
            "REAL_TYPE", "STRINGLIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

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
                  "IDENTIFIER", "CHARACTER", "INTEGER_TYPE", "REAL_TYPE", 
                  "EXPONENT", "STRINGLIT", "WS", "STRING_S", "ESC", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[84] = self.STRINGLIT_action 
            actions[88] = self.ERROR_CHAR_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.UNCLOSE_STRING_action 
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
                    
     


