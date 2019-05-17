.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x1 Z
.field static y1 Z
.field static z1 Z
.field static x2 I
.field static y2 I
.field static z2 I
.field static x3 F
.field static y3 F
.field static z3 F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_1
	iand
	ifle Label7
	iconst_3
	iconst_2
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_1
	iand
	ifle Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	putstatic MPClass.z1 Z
	getstatic MPClass.z1 Z
	putstatic MPClass.y1 Z
	getstatic MPClass.y1 Z
	putstatic MPClass.x1 Z
	getstatic MPClass.x1 Z
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.y1 Z
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.z1 Z
	invokestatic io/putBoolLn(Z)V
	bipush 15
	bipush 25
	iconst_5
	irem
	iadd
	bipush 12
	iconst_5
	imul
	iconst_5
	irem
	iadd
	bipush 15
	bipush 10
	idiv
	iadd
	putstatic MPClass.z2 I
	getstatic MPClass.z2 I
	putstatic MPClass.y2 I
	getstatic MPClass.y2 I
	putstatic MPClass.x2 I
	getstatic MPClass.x2 I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.y2 I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.z2 I
	invokestatic io/putIntLn(I)V
	bipush 30
	i2f
	bipush 15
	i2f
	fdiv
	putstatic MPClass.z3 F
	getstatic MPClass.z3 F
	putstatic MPClass.y3 F
	getstatic MPClass.y3 F
	putstatic MPClass.x3 F
	getstatic MPClass.x3 F
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.y3 F
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.z3 F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 8
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
