.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is ie I from Label0 to Label1
.var 2 is jr I from Label0 to Label1
.var 3 is kt I from Label0 to Label1
.var 4 is cuo I from Label0 to Label1
Label0:
	iconst_0
	istore 4
	bipush 9
	istore_1
Label2:
	iload_1
	iconst_1
	if_icmplt Label4
	bipush 8
	istore_2
Label5:
	iload_2
	iconst_1
	if_icmplt Label7
	bipush 7
	istore_3
Label8:
	iload_3
	iconst_1
	if_icmplt Label10
	iload 4
	iconst_1
	iadd
	istore 4
Label9:
	iload_3
	iconst_1
	isub
	istore_3
	goto Label8
Label10:
Label6:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label5
Label7:
Label3:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label2
Label4:
	iload 4
	bipush 7
	bipush 8
	imul
	bipush 9
	imul
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
.limit locals 5
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
