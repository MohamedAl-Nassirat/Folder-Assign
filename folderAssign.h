#ifndef SORT_DATASET_H
#define SORT_DATASET_H

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>

#define MAX_FILENAME_LEN 256
#define MAX_FILE_COUNT 1000

void create_dir(char *dir_name);
int read_dir(char *dir_name);
void copy_file(char *src_dir, char *dst_dir, char *filename);

#endif
