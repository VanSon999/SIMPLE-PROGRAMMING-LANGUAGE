.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.2300
	ldc 1.2300
	fcmpl
	ifeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1000
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1900
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 0.2000
	fcmpl
	ifge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1100
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 0.1000
	fneg
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1200
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	iconst_1
	i2f
	ldc 0.2300
	fadd
	fcmpl
	ifne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1000
	fcmpl
	iflt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	iconst_1
	i2f
	fcmpl
	iflt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 1.2300
	fcmpl
	iflt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 2.1000
	fcmpl
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 0.1200
	fcmpl
	ifgt Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	invokestatic io/putBool(Z)V
	ldc 1.2300
	ldc 1.2300
	fcmpl
	ifgt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 29
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
