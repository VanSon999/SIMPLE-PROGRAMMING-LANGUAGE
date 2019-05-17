.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is Sum I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_2
Label2:
	iload_1
	bipush 20
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 17
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	goto Label3
Label9:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	goto Label2
Label13:
	iload_2
	iload_1
	iadd
	istore_2
	goto Label2
Label3:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 8
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
