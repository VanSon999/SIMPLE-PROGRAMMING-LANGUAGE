.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_0
	ior
	ifgt Label2
	iconst_1
	iconst_0
	ior
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_0
	ior
	ifgt Label4
	iconst_0
	iconst_0
	ior
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_0
	ior
	ifgt Label6
	iconst_1
	iconst_0
	ior
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_0
	ior
	ifgt Label8
	iconst_0
	iconst_0
	ior
	ifgt Label8
	iconst_0
	goto Label9
Label8:
	iconst_1
Label9:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iand
	ifle Label11
	iconst_1
	iconst_1
	iand
	ifle Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iand
	ifle Label13
	iconst_0
	iconst_1
	iand
	ifle Label13
	iconst_1
	goto Label12
Label13:
	iconst_0
Label12:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	iand
	ifle Label15
	iconst_1
	iconst_1
	iand
	ifle Label15
	iconst_1
	goto Label14
Label15:
	iconst_0
Label14:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	iand
	ifle Label17
	iconst_0
	iconst_1
	iand
	ifle Label17
	iconst_1
	goto Label16
Label17:
	iconst_0
Label16:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 26
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
