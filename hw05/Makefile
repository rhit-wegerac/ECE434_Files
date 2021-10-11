
-include ./path.mak

CFLAGS := -g
LINKER_FLAGS := -lstdc++

all:
        $(CC) $(CFLAGS) -c app.c -o app.o
        $(CC) $(CFLAGS) app.o -o app.arm
        
app.arm : app.o
        @echo; echo $@ successfully created; echo
        $(CC) $(CFLAGS)  app.o -o app.arm

app.o : app.c
        $(CC) $(CFLAGS) -c app.c -o app.o

clean:
        rm -rf app.arm
        rm -rf app.o    
