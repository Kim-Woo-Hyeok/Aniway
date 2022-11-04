from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,
                    email,
                    name,
                    date_of_birth,
                    password,
                    gender,
                    phone,
                    pet_name,
                    pet_gender,
                    pet_breed,
                    pet_weight,
                    pet_neuter,
                    pet_date_of_birth,
                    ):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
            gender=gender,
            phone=phone,
            pet_name=pet_name,
            pet_gender=pet_gender,
            pet_breed=pet_breed,
            pet_weight=pet_weight,
            pet_neuter=pet_neuter,
            pet_date_of_birth=pet_date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, password):
        user = self.create_user(
            email,
            name,
            date_of_birth,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

