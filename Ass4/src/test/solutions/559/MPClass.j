.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static y F
.field static z Z

.method public static foo(IFZ)F
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c Z from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
	fload_1
	invokestatic io/putFloatLn(F)V
	iload_2
	invokestatic io/putBoolLn(Z)V
	bipush 10
	istore_0
	ldc 10.0000
	fstore_1
	iconst_1
	istore_2
	iload_0
	invokestatic io/putIntLn(I)V
	fload_1
	invokestatic io/putFloatLn(F)V
	iload_2
	invokestatic io/putBoolLn(Z)V
	ldc 10.0000
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
.var 1 is i F from Label2 to Label3
Label2:
	iconst_5
	putstatic MPClass.x I
	ldc 5.0000
	putstatic MPClass.y F
	iconst_0
	putstatic MPClass.z Z
	getstatic MPClass.x I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.y F
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.z Z
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.x I
	getstatic MPClass.y F
	getstatic MPClass.z Z
	invokestatic MPClass/foo(IFZ)F
	fstore_1
	getstatic MPClass.x I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.y F
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.z Z
	invokestatic io/putBoolLn(Z)V
Label3:
	return
.limit stack 5
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
