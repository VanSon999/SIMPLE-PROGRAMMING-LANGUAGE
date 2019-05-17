.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ctx I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iy I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	putstatic MPClass.ctx I
	iconst_1
	istore_1
Label2:
	iload_1
	bipush 9
	if_icmpgt Label4
Label5:
	iload_1
	bipush 9
	if_icmpeq Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	bipush 9
	istore_1
Label9:
.var 2 is ast I from Label9 to Label10
	getstatic MPClass.ctx I
	invokestatic io/putInt(I)V
Label10:
	goto Label5
Label6:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
Label1:
	return
.limit stack 5
.limit locals 3
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
