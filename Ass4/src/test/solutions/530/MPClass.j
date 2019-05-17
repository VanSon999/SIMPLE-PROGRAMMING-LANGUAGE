.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is k I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_4
	if_icmpgt Label4
	iload_1
	iconst_1
	iadd
	istore_2
Label5:
	iload_2
	iconst_4
	if_icmpgt Label7
	iload_1
	iload_2
	imul
	invokestatic io/putIntLn(I)V
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label5
Label7:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iconst_1
	istore_1
Label8:
	iload_1
	bipush 10
	if_icmpgt Label10
	iconst_0
	istore_3
	iload_3
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label13
	iconst_5
	istore_1
	goto Label14
Label13:
	goto Label10
Label14:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
Label1:
	return
.limit stack 7
.limit locals 4
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
