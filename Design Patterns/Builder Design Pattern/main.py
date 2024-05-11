from engineerbuilder import EngineerBuider

def main():
    eng_builder = EngineerBuider()
    
    eng_student = eng_builder.set_name("Div") \
                    .set_age("24") \
                    .set_subjects("DSA") \
                    .build()

    print(eng_student)


if __name__ == "__main__":
    main()