.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static irt I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	ineg
	putstatic MPClass.irt I
Label2:
	getstatic MPClass.irt I
	bipush 100
	if_icmpgt Label4
	iconst_0
	putstatic MPClass.irt I
Label5:
	getstatic MPClass.irt I
	bipush 100
	if_icmpgt Label7
Label6:
	getstatic MPClass.irt I
	iconst_1
	iadd
	putstatic MPClass.irt I
	goto Label5
Label7:
Label3:
	getstatic MPClass.irt I
	iconst_1
	iadd
	putstatic MPClass.irt I
	goto Label2
Label4:
	getstatic MPClass.irt I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
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
