.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	iand
	ifle Label3
	iconst_0
	iconst_1
	iand
	ifle Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iand
	ifle Label5
	iconst_1
	iconst_1
	iand
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	iand
	ifle Label7
	iconst_1
	iconst_1
	iand
	ifle Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	iand
	ifle Label9
	iconst_0
	iconst_1
	iand
	ifle Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	iand
	ifle Label13
	iconst_0
	bipush 6
	idiv
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iconst_1
	iand
	ifle Label13
	iconst_1
	goto Label12
Label13:
	iconst_0
Label12:
	invokestatic io/putBoolLn(Z)V
	goto Label1
Label1:
	return
.limit stack 18
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
