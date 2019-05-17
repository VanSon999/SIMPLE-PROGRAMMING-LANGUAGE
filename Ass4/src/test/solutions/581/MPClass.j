.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	ldc 100000
	if_icmpgt Label4
	sipush 10000
	istore_2
Label5:
	iload_2
	iconst_1
	if_icmplt Label7
Label8:
.var 3 is i I from Label8 to Label9
	iconst_1
	istore_3
	iload_2
	sipush 9999
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	goto Label7
Label13:
Label9:
Label6:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label5
Label7:
	iload_1
	ldc 99995
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iload_1
	i2f
	invokestatic io/putFloatLn(F)V
	goto Label4
	goto Label17
Label16:
	goto Label3
Label17:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
Label1:
	return
.limit stack 8
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
