.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static tong(II)I
.var 0 is aet I from Label0 to Label1
.var 1 is biy I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_1
	bipush 10
	invokestatic MPClass/tong(II)I
	bipush 10
	iconst_1
	invokestatic MPClass/tong(II)I
	isub
	invokestatic io/putInt(I)V
Label3:
	return
.limit stack 3
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
