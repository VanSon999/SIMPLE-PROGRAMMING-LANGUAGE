.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static y I

.method public static foo1()Z
Label0:
	bipush 10
	putstatic MPClass.x I
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static foo2()Z
Label2:
	bipush 10
	putstatic MPClass.y I
	iconst_1
	goto Label3
Label3:
	ireturn
.limit stack 3
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label4 to Label5
.var 1 is i I from Label4 to Label5
Label4:
	iconst_5
	putstatic MPClass.x I
	iconst_5
	putstatic MPClass.y I
	iconst_1
	iconst_1
	iadd
	iconst_2
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_1
	iand
	ifle Label9
	invokestatic MPClass/foo1()Z
	iconst_1
	iand
	ifle Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iadd
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic MPClass/foo2()Z
	iand
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.x I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.y I
	invokestatic io/putIntLn(I)V
Label5:
	return
.limit stack 9
.limit locals 2
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
