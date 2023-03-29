#include <stdio.h>
#include <cpuid.h>
#include <stdint.h>
#include <openssl/md5.h>
#include <string.h>

void calc_md5(char *str, size_t len, unsigned char *digest) {
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, str, len);
    MD5_Final(digest, &ctx);
}

void bytes_to_hex_string(const unsigned char* bytes, int num_bytes, char* hex_string) {
    for (int i = 0; i < num_bytes; i++) {
        sprintf(&hex_string[i * 2], "%02x", bytes[0xf-i]);
    }
}

int main() {
    int leaf = 1;

    uint32_t eax = 3, ebx = 0, ecx = 0, edx = 0;


    if (__get_cpuid(leaf, &eax, &ebx, &ecx, &edx))
    {
        printf("leaf=%d, eax=0x%x, ebx=0x%x, ecx=0x%x, edx=0x%x\n",
               leaf, eax, ebx, ecx, edx);
    }

    uint32_t local_18 = eax << 0x18 | eax >> 0x18 | (eax & 0xff00) << 8 | eax >> 8 & 0xff00;
    uint32_t local_14 =  edx << 0x18 | edx >> 0x18 | (edx & 0xff00) << 8 | edx >> 8 & 0xff00;
    char PSN[0x11];
    snprintf(PSN,0x11,"%08X%08X",(long)local_18,(long)local_14);
    printf("%s\n",PSN);

    char md5digit[MD5_DIGEST_LENGTH];

    calc_md5(PSN, 0x10, md5digit);

    char md5decode[33];

    bytes_to_hex_string(md5digit,16,md5decode);
    printf("%s\n", md5decode);
    return 0;
}
