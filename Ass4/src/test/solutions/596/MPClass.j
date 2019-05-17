.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ast F
.field static byz F
.field static ctx F
.field static out Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 400
	i2f
	putstatic MPClass.ctx F
	getstatic MPClass.ctx F
	sipush 400
	i2f
	iconst_1
	i2f
	fdiv
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	getstatic MPClass.ctx F
	sipush 200
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	goto Label1
Label9:
	goto Label5
Label4:
	ldc "Hello"
	invokestatic io/putString(Ljava/lang/String;)V
Label5:
Label1:
	return
.limit stack 5
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
