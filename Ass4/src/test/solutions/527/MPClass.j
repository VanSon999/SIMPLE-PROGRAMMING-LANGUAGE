.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	iadd
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_2
	isub
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_2
	imul
	invokestatic io/putIntLn(I)V
	iconst_1
	iconst_2
	idiv
	invokestatic io/putIntLn(I)V
	bipush 31
	iconst_4
	irem
	invokestatic io/putIntLn(I)V
	iconst_1
	i2f
	iconst_2
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	iconst_1
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_2
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	goto Label1
Label1:
	return
.limit stack 7
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
