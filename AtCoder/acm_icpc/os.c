// #include <stdio.h>
// #include <sys/types.h>
// #include <unistd.h>
// #include <sys/wait.h>

// // void main(){
// //   pid_t pid;
// //   int status;
// //   printf("P: parent\n");
// //   sleep(10);
// //   if ((pid = fork()) !=0){
// //     printf("P:child created\n");
// //     wait(&status)
// //     printf("P: child exited\n");
// //     sleep(10);
// //   }else{
// //     printf("C: child\n");
// //     sleep(10);
// //     printf("C: exiting\n");
// //     exit(0);
// //   }
// // }

// void main(){
//   pid_t pid;
//   int status;
//   if ((pid=fork())!=0){
//     wait(&status);
//   }else{
//     execlp("ls","ls",NULL);
//   }
// }
#include <stdio.h>
#include <pthread.h>

/*
   スレッドの利用法

   compile:
   gcc -o thread thread.c

   run:
   thread
*/

// void * f(void * x) {
//   int i;
//   for (i = 0; i < 1000000; i++) {
//     printf("thread %ld said %dth hello\n", (long)x, i);
//   }
//   return 0;
// }

// main()
// {
//   pthread_t tidx, tidy;
//   //pthread_attr_t attr;
//   //pthread_attr_init(&attr);
//   /* f(0) を実行するスレッド */
//   pthread_create(&tidx, NULL, f, (void *)0);
//   /* f(1) を実行するスレッド */
//   pthread_create(&tidy, NULL, f, (void *)1);
//   /* 最初のスレッドの終了待ち */
//   pthread_join(tidx, 0);
//   /* 2個目のスレッドの終了待ち */
//   pthread_join(tidy, 0);
// }

#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>

// main()
// {
//   int cid;
//   cid = fork();
//   if (cid == 0) {
//     /* child */
//     execl("/usr/bin/firefox", "firefox", NULL);
//     printf("could not run the program\n");
//   } else {
//     int stat;
//     wait(&stat);
//   }
// }


/* this program illustrates how to use signals (event notification in Unix-like OSes)
   with its simplest example.
   divide by zero generates floating point exception (SIGFPE) and a handler prints
   a message and die. */
// #include <signal.h>


// hoge()
// {
//     int x = 1;
//     int y = 0;
//     int z = x / y;
//     printf("ok\n");
// }

// void my_sigfpe_handler(int signum)
// {
//   printf("divide by zero\n");
//   exit(1);
// }

// main()
// {
//   struct sigaction a[1];
//   a->sa_handler = my_sigfpe_handler;
//   sigemptyset(&a->sa_mask);
//   a->sa_flags = 0;
//   sigaction(SIGFPE, a, 0);
//   hoge();
// }
#include <pthread.h>

/*
   スレッドの利用法

   compile:
   gcc -o mutex mutex.c

   run:
   mutex
*/

// pthread_mutex_t mutex;
// int counter;

// void * f(void * x) {
//   int i;
//   for (i = 0; i < 100; i++) {
//     pthread_mutex_lock(&mutex);
//     printf("thread %d: counter = %d\n", x, counter);
//     counter++;
//     pthread_mutex_unlock(&mutex);
//   }
//   return 0;
// }

// main()
// {
//   pthread_t tidx, tidy;
//   pthread_attr_t attr;
//   pthread_attr_init(&attr);
//   pthread_mutex_init(&mutex, NULL);
//   /* f(0) を実行するスレッド */
//   pthread_create(&tidx, &attr, f, (void *)0);
//   /* f(1) を実行するスレッド */
//   pthread_create(&tidy, &attr, f, (void *)1);
//   /* 最初のスレッドの終了待ち */
//   pthread_join(tidx, 0);
//   /* 2個目のスレッドの終了待ち */
//   pthread_join(tidy, 0);
// }

// #include <sys/time.h>

// main() {
//   int i;
//   struct timeval tp[2];
//   gettimeofday(tp, 0);
//   for (i = 0; i < 1000000; i++) {
//     do_nothing();
//   }
//   gettimeofday(tp + 1, 0);
//   {
//     int dt = (tp[1].tv_sec - tp[0].tv_sec) * 1000000
//       + (tp[1].tv_usec - tp[0].tv_usec);
//     if (dt % 10000 == 0) {
//       printf("%d usec (suspsect this is not high-resolution timer)\n", dt);
//     } else {
//       printf("%d usec\n", dt);
//     }
//   }
// }

// int do_nothing()
// {
//   return 3;
// }

/* this program illustrates how */

#include <signal.h>
#include <sys/mman.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
//#include <asm/sigcontext.h>

#define PAGESIZE 4096

char a[PAGESIZE]
__attribute__ ((aligned(PAGESIZE)));

void my_sigsegv_handler(int sig, siginfo_t *scp,
        void *context) {
  char * b = scp->si_addr;
  printf("  sig=%d\n", sig);
  printf("  violation when accessing %p\n", b);
  {
    char * c = (char*)(((unsigned long)b) & ~(PAGESIZE - 1));
    assert(c <= b);
    assert(b < c + PAGESIZE);
    printf("  unprotecting [%p,%p)\n", c, c + PAGESIZE);
    int r = mprotect(c, PAGESIZE, PROT_READ | PROT_WRITE);
    if (r != 0) { perror("mprotect"); exit(1); }
    assert(r == 0);
  }
}

// int main() {
//   /* segmantion fault縺ｮ繝上Φ繝峨Λ
//      (fault縺励◆繝壹�繧ｸ縺ｫ繧｢繧ｯ繧ｻ繧ｹ讓ｩ繧貞�縺�)
//      繧定ｨｭ螳� */
//   struct sigaction act;
//   act.sa_flags = SA_SIGINFO;
//   act.sa_sigaction = my_sigsegv_handler;
//   sigemptyset(&act.sa_mask);
// #if 1
//   sigaction(SIGSEGV, &act, 0);
// #endif

//   /* 驟榊�a繧定ｪｭ縺ｿ譖ｸ縺堺ｸ榊庄縺ｫ險ｭ螳� */
//   printf("protecting [%p,%p)\n", a, a + PAGESIZE);
//   int r = mprotect(a, PAGESIZE, PROT_NONE);
//   assert(r == 0);

//   /* a繧偵い繧ｯ繧ｻ繧ｹ
//      -> segumantation fault
//      -> a縺瑚ｪｭ縺ｿ譖ｸ縺榊庄縺ｫ縺ｪ繧�
//      -> 蜀榊ｮ溯｡�
//      -> 繧｢繧ｯ繧ｻ繧ｹ謌仙粥 */
//   printf("accessing %p\n", a);
//   a[5] = 0;
//   printf("successfully accessed %p\n", a);
//   return 0;
// }

// #include <sys/types.h>
// #include <sys/stat.h>
// #include <fcntl.h>
// #include <unistd.h>
// #include <stdlib.h>
// #include <sys/mman.h>
// #include <stdio.h>

// int main() {
//   int fd;
//   struct stat buf[1];
//   if (-1 == (fd = open("map.c", O_RDONLY))) {
//     perror("open");
//     exit(1);
//   } else if (-1 == stat("map.c", buf)) {
//     perror("stat");
//     exit(1);
//   } else {
//     char * a = mmap(0, buf->st_size,
//         PROT_READ | PROT_WRITE, MAP_PRIVATE,
//         fd, 0);
//     if (a == MAP_FAILED) { perror("mmap"); exit(1); }
//     int i;
//     for (i = 0; i < buf->st_size; i++) {
//       putchar(a[i]);
//     }
//   }
//   return 0;
// }
// #include <sys/types.h>
// #include <sys/socket.h>
// #include <netinet/in.h>
// #include <assert.h>
// #include <stdio.h>

// #define HELLO_MR_SERVER "hello, Mr. server"

// void sock_error()
// {
//   perror("");
//   exit(1);
// }

// int main()
// {
//   int s, new_s;
//   int l;
//   struct sockaddr_in a;
//   /* make socket */
//   if (-1 == (s = socket(AF_INET, SOCK_STREAM, 0)))
//     sock_error();

//   /* assign port */
//   a.sin_family = AF_INET;
//   a.sin_addr.s_addr = INADDR_ANY;
//   a.sin_port = htons(5000);
//   if (-1 == bind(s, (struct sockaddr *)&a, sizeof(a)))
//     sock_error();

//   /* specify queue length */
//   if (-1 == listen(s, 1))
//     sock_error();

//   l = sizeof(a);
//   if (-1 == getsockname(s,  (struct sockaddr *)&a, &l))
//     sock_error();

//   printf("accepting connection at port %d...\n", ntohs(a.sin_port));
//   l = sizeof(a);
//   if (-1 == (new_s = accept(s, (struct sockaddr *)&a, &l)))
//     sock_error();

//   {
//     /* now ready to receive stuff */
//     char buffer[100];
//     int expect_len = strlen(HELLO_MR_SERVER) + 1;
//     printf("receiving\n");
//     if (expect_len != recv(new_s, buffer, expect_len, 0))
//       sock_error();
//     printf("received: %s\n", buffer);
//     printf("done\n");
//   }
//   return 0;
// }
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <assert.h>
#include <stdio.h>

#define HELLO_MR_SERVER "hello, Mr. server"

void sock_error()
{
  perror("");
  exit(1);
}

int main()
{
  int s;
  struct hostent * hp;
  struct sockaddr_in a;
  short port = 5000;
  char * buffer = HELLO_MR_SERVER;
  int len = strlen(buffer) + 1;

  //declaration
  if (-1 == (s = socket(AF_INET, SOCK_STREAM, 0)))
    sock_error();

  /* get server address */
  if (0 == (hp = gethostbyname("localhost")))
    sock_error();

  /* connect to server */
  a.sin_family = AF_INET;
  a.sin_addr.s_addr = *((unsigned long *)hp->h_addr);
  a.sin_port = htons(port);

  printf("connecting to server localhost:%d\n", port);
  if (-1 == connect(s, (struct sockaddr *)&a, sizeof(a)))
    sock_error();

  printf("sending\n");
  if (len != send(s, buffer, len, 0))
    sock_error();

  printf("done\n");
}

