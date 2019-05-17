.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ast F
.field static byz F
.field static ctx F
.field static out Z

.method public static foo(F)F
.var 0 is ctx F from Label0 to Label1
Label0:
	fload_0
	iconst_0
	i2f
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	ldc 1.3000
	goto Label1
	goto Label5
Label4:
	ldc 1.2000
	goto Label1
Label5:
Label1:
	freturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label6 to Label7
Label6:
	iconst_0
	i2f
	putstatic MPClass.ctx F
Label8:
	iconst_1
	ifle Label9
	iconst_3
	i2f
	putstatic MPClass.ctx F
	getstatic MPClass.ctx F
	iconst_3
	i2f
	fcmpl
	ifne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label8
	goto Label13
Label12:
	goto Label9
Label13:
	goto Label8
Label9:
	getstatic MPClass.ctx F
	iconst_3
	i2f
	fcmpl
	ifeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
Label18:
	getstatic MPClass.ctx F
	iconst_3
	i2f
	fcmpl
	ifne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label19
	getstatic MPClass.ctx F
	invokestatic io/putFloat(F)V
	getstatic MPClass.ctx F
	iconst_1
	i2f
	fsub
	putstatic MPClass.ctx F
	goto Label19
	goto Label18
Label19:
	goto Label17
Label16:
Label17:
Label7:
	return
.limit stack 12
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
