.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
Label0:
	iconst_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	invokestatic io/putBoolLn(Z)V
	bipush 12
	i2f
	iconst_5
	i2f
	fdiv
	bipush 9
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iconst_4
	iconst_4
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 11
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
