.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static fact(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifgt Label6
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fact(I)I
	imul
	goto Label1
	goto Label7
Label6:
	iconst_1
	goto Label1
Label7:
Label1:
	ireturn
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label8 to Label9
Label8:
	iconst_5
	putstatic MPClass.a I
	getstatic MPClass.a I
	invokestatic MPClass/fact(I)I
	invokestatic io/putIntLn(I)V
Label9:
	return
.limit stack 6
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
