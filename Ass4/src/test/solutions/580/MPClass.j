.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static too(I)Z
.var 0 is n I from Label0 to Label1
.var 1 is at I from Label0 to Label1
.var 2 is bz I from Label0 to Label1
.var 3 is iy I from Label0 to Label1
Label0:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
.var 1 is a I from Label2 to Label3
Label2:
	iconst_1
	invokestatic MPClass/too(I)Z
	invokestatic io/putBool(Z)V
Label3:
	return
.limit stack 2
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
