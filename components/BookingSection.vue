<template>
<div class="container-fluid">
    <div class="section-padding pt-0 border-b-1 border-bordercolor">
        <div class="flex justify-between gap-y-10 lg:flex-row flex-col">
            <div class="lg:w-1/3 w-full">
                <div class="max-w-[360px]">
                    <div class="mb-10">
                        <p>Specify your check-in and check-out dates and the number of people – find the best room rate and book it online easily.</p>
                    </div>
                    <div class="mb-10">
                        <h3 class="text-2xl mb-4">Note</h3>
                        <ul class="booking-sidebar-time">
                            <li class="font-bold block text-black mb-1">Check-in time: <span class="font-normal text-dark">02:00PM</span></li>
                            <li class="font-bold block text-black mb-1">Check-out time: <span class="font-normal text-dark">12:00PM</span></li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-2xl mb-4">Cancellation policy</h3>
                        <p>Free cancellation within 48 hours after successful booking and 5 days before check-in time. Then, cancel the room 5 days before the check-in time, 100% refund of the total amount paid (minus the service fee). <n-link to="/contact">Details</n-link></p>
                    </div>
                </div>
            </div>
            <div class="lg:w-2/3 w-full">
                <div class="lg:pl-[100px] pl-0">
                    <form id="contact-form" class="grid gap-7 grid-cols-2" action="#" method="POST">
                        <div class="single-fild col-span-2 sm:col-span-1">
                            <label class="block mb-3 text-black" for="check-in-date">CHECK-IN <span class="ml-[3px] text-[#F56C6C]">*</span></label>
                            <client-only><date-picker id="check-in-date" placeholder="Select Check In Date" format="MM/dd/yyyy" /></client-only>
                        </div>
                        <div class="single-fild col-span-2 sm:col-span-1">
                            <label class="block mb-3 text-black" for="check-out-date">CHECK-OUT <span class="ml-[3px] text-[#F56C6C]">*</span></label>
                            <client-only><date-picker id="check-out-date" placeholder="Select Check Out Date" format="MM/dd/yyyy" /></client-only>
                        </div>
                        <div class="single-fild col-span-2">
                            <label class="block mb-3 text-black" for="adults">ADULTS <span class="ml-[3px] text-[#F56C6C]">*</span></label>
                            <select class="form-control booking-select text-[15px] relative block w-full py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" name="adults" id="adults">
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                                <option value="6">6</option>
                            </select>
                        </div>
                        <div class="single-fild col-span-2">
                            <label class="block mb-3 text-black" for="children">CHILDRENS (from 2-12 years old) <span class="ml-[3px] text-[#F56C6C]">*</span></label>
                            <select class="form-control booking-select text-[15px] relative block w-full py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0" name="adults" id="children">
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                            </select>
                        </div>
                        <ButtonDefault
                            :btnLink="'/booking'"
                            :btnClass="'min-w-[220px] min-h-[50px] md:min-h-[60px] py-2 sm:py-5 btn text-center relative overflow-hidden h-[54px] lg:h-[60px] px-[30px] lg:px-[40px] text-[14px] flex items-center justify-center btn-primary btn-hover-dark'"
                            :btnText="'Booking Now'"
                            :btnClassParent="'flex text-center leading-[1]'"
                        />
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    components: {
    },
    data () {
        return {
            date_today:new Date()
        }
    }
}
</script>

<style lang="scss">
.vdp-datepicker {
    & input {
       @apply text-[15px] relative block w-full py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0;
    }
   
}
.booking-select{
    option{
       @apply text-[15px] relative block w-full py-4 px-4 transition-all duration-500 text-[#515151] border-1 border-[#ced4da] bg-transparent focus:border-black focus:shadow-none focus-visible:outline-0;
    }
}
</style>