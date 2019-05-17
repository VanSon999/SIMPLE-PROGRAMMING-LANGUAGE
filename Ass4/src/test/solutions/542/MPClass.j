.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo1()Ljava/lang/String;
Label0:
	ldc "Ass 4"
	goto Label1
Label1:
	areturn
.limit stack 1
.limit locals 0
.end method

.method public static foo2()F
Label2:
	ldc 12.0256
	goto Label3
Label3:
	freturn
.limit stack 1
.limit locals 0
.end method

.method public static foo3()I
Label4:
	iconst_2
	goto Label5
Label5:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static foo4()Z
Label6:
	iconst_1
	goto Label7
Label7:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label8 to Label9
Label8:
	invokestatic MPClass/foo1()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MPClass/foo2()F
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/foo3()I
	invokestatic io/putIntLn(I)V
	invokestatic MPClass/foo4()Z
	invokestatic io/putBoolLn(Z)V
Label9:
	return
.limit stack 2
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
