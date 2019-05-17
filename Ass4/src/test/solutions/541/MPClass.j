.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is s1 I from Label0 to Label1
.var 4 is s2 I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iconst_0
	istore 4
	bipush 10
	istore_1
Label2:
	iload_1
	iconst_1
	if_icmplt Label4
	iload_3
	iload_1
	iadd
	istore_3
	iconst_1
	istore_2
Label5:
	iload_2
	bipush 10
	if_icmpgt Label7
	iload 4
	iload_2
	iadd
	istore 4
	iload_2
	bipush 7
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	goto Label7
Label11:
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
	isub
	istore_1
	goto Label2
Label4:
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putIntLn(I)V
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
