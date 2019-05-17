.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static z I

.method public static foo(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_2
	imul
	istore_0
	iload_1
	iconst_2
	imul
	istore_1
	iload_2
	iconst_2
	imul
	istore_2
	iload_0
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_1
	putstatic MPClass.a I
	iconst_2
	putstatic MPClass.b I
	iconst_3
	putstatic MPClass.c I
	getstatic MPClass.a I
	getstatic MPClass.b I
	getstatic MPClass.c I
	invokestatic MPClass/foo(III)I
	putstatic MPClass.z I
	getstatic MPClass.a I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.b I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.c I
	invokestatic io/putIntLn(I)V
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
