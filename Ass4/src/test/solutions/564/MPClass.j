.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is tong I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 9
	if_icmpgt Label4
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpeq Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label7
	goto Label8
Label7:
	goto Label3
Label8:
	iload_3
	iload_1
	iadd
	istore_3
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
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
