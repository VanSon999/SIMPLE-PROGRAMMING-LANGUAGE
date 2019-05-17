.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is s I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	bipush 10
	istore_1
Label2:
	iload_1
	iconst_1
	if_icmplt Label4
	iload_2
	iload_1
	iadd
	istore_2
	goto Label4
Label3:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label2
Label4:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
