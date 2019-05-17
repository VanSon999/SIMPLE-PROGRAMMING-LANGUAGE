.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is ast I from Label0 to Label1
.var 2 is byz I from Label0 to Label1
.var 3 is ctx I from Label0 to Label1
.var 4 is out Z from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	iconst_0
	if_icmplt Label4
	bipush 10
	istore_3
Label5:
	iload_3
	iconst_0
	if_icmplt Label7
	iload_3
	invokestatic io/putInt(I)V
Label6:
	iload_3
	iconst_1
	isub
	istore_3
	goto Label5
Label7:
Label3:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label2
Label4:
Label1:
	return
.limit stack 4
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
