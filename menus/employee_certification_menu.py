from dto.employee_certification_dto import CloseToExpirationDTO


class EmployeeCertificationMenu():

    @staticmethod
    def display_close_to_expiration(closes: list[CloseToExpirationDTO]):
        print("*********************************************************************************************************")
        print(f"{'Employee':<50}|{'Certification':<25}|Expiration Date")
        print("__________________________________________________________________________________________________________")
        if len(closes)==0:
            print("NO CERTIFICATION IN END OF LIFE")
            print("*********************************************************************************************************")
            return
        for close in closes:
            name = close.employee_first_name + " " + close.employee_last_name
            print(f"{name:<50}|{close.certification_name:<25}|{close.expiration_date}")
            print("*********************************************************************************************************")