import { Injectable } from '@nestjs/common';

import { HttpService } from '@nestjs/axios';

import { firstValueFrom } from 'rxjs';

@Injectable()
export class ExpenseService {

    constructor(
        private readonly httpService: HttpService
    ) {}

    async submitExpense(
        body: any
    ) {

        const response = await firstValueFrom(

            this.httpService.post(
                'http://localhost:8000/submit-expense',
                body
            )
        );

        return response.data;
    }
}