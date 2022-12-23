#include "folderAssign.h"

#define MAX_FILENAME_LEN 256
#define MAX_FILE_COUNT 1000

char training_dir[MAX_FILENAME_LEN];
char validation_dir[MAX_FILENAME_LEN];
char images_dir[MAX_FILENAME_LEN];

int file_count;
char file_names[MAX_FILE_COUNT][MAX_FILENAME_LEN];

void create_dir(char *dir_name) {
  struct stat st = {0};
  if (stat(dir_name, &st) == -1) {
      mkdir(dir_name, 0700);
  }
}

int read_dir(char *dir_name) {
  DIR *dir;
  struct dirent *ent;
  file_count = 0;
  if ((dir = opendir (dir_name)) != NULL) {
    while ((ent = readdir (dir)) != NULL) {
      if (strcmp(ent->d_name, ".") == 0 || strcmp(ent->d_name, "..") == 0) {
        continue;
      }
      strcpy(file_names[file_count], ent->d_name);
      file_count++;
    }
    closedir (dir);
  } else {
    perror ("");
    return -1;
  }
  return 0;
}

void copy_file(char *src_dir, char *dst_dir, char *filename) {
  char src_path[MAX_FILENAME_LEN];
  char dst_path[MAX_FILENAME_LEN];
  sprintf(src_path, "%s/%s", src_dir, filename);
  sprintf(dst_path, "%s/%s", dst_dir, filename);

  FILE *src_file = fopen(src_path, "r");
  if (src_file == NULL) {
    perror("Error opening source file");
    return;
  }
  


  FILE *dst_file = fopen(dst_path, "w");
  if (dst_file == NULL) {
    perror("Error opening destination file");
    fclose(src_file);
    return;
  }

  char buffer[MAX_FILENAME_LEN];
  while (fgets(buffer, MAX_FILENAME_LEN, src_file) != NULL) {
    fputs(buffer, dst_file);
  }

  fclose(src_file);
  fclose(dst_file);
}


int main(int argc, char **argv) {
  if (argc != 4) {
    printf("Usage: ./sort_dataset <images_dir> <training_dir> <validation_dir>\n");
    return -1;
  }
  strcpy(images_dir, argv[1]);
  strcpy(training_dir, argv[2]);
  strcpy(validation_dir, argv[3]);
  create_dir(training_dir);
  create_dir(validation_dir);
  if (read_dir(images_dir) != 0) {
    printf("Error reading images directory\n");
    return -1;
  }
  int i;
  printf("Enter the percentage of files to be split into the training set (0-100): ");
  int training_percentage;
  scanf("%d", &training_percentage);

    for (i = 0; i < file_count; i++) {
    if (i < (file_count * training_percentage / 100)) {
      copy_file(images_dir, training_dir, file_names[i]);
    } else {
      copy_file(images_dir, validation_dir, file_names[i]);
    }
  }
}

