.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is res I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	istore_2
	iload_1
	iload_2
	invokestatic MPClass/foo(II)I
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static foo(II)I
.var 0 is a I from Label2 to Label3
.var 1 is b I from Label2 to Label3
Label2:
	iload_0
	iload_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	sipush 222
	goto Label3
	goto Label7
Label6:
	bipush 111
	goto Label3
Label7:
Label3:
	ireturn
.limit stack 4
.limit locals 2
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
