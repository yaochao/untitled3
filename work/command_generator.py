#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2018/12/3


import os

tables = "cdh_birthmedicine,cdh_checkup,cdh_deadregister,cdh_defectregister,cdh_nutritionaldiseases,cdh_screeningrecord,cli_diagnose,cli_fee_detail,cli_fee_invoice,cli_recipe,cli_register,cli_seerecord,dc_aidsprevention,dc_chronicfilariasis,dc_damagedetection,dc_deathrecord,dc_infectiousdiseases,dc_occupationaldisease,dc_occupationalhealth,dc_pesticidepoisoning,dc_riskbehavioral,dc_schistosomiasis,dc_tbrecord,dc_vaccination,dm_hepatitisb,ehr_cjqk,ehr_healthrecord,ehr_hjblys,ehr_jwgms,ehr_jwjbs,ehr_jwsss,ehr_jwsxs,ehr_jwwss,ehr_jzjbs,emr_inhrecord,emr_outhrecord,inh_diag,inh_inhos,inh_orders,inh_outhos,inh_settle,inh_settle_detail,ipt_afteranesthesiair,ipt_anesthesiarecords,ipt_checkingrecordsd,ipt_chinafirstpagemedica,ipt_consultationrecord,ipt_dailycourser,ipt_examinationrecord,ipt_hospitalsignsre,ipt_preoperativediscussion,ipt_preoperativesummary,ipt_recordfirstduration,ipt_salvagelogging,ipt_summary,lis_report_auti,lis_report_bacteria,lis_report_detail,lis_report_info,mdc_diabetesmedicine,mdc_diabetesrecord,mdc_diabetesvisit,mdc_hypertensionmedicine,mdc_hypertensionvisit,mdc_hypertesiorecord,mdc_oldpeoplemedicine,mdc_oldpeoplerecord,mdc_oldpeoplevisit,mdc_tumourrecord,mdc_tumourvisit,med_dispense,mhc_birthcontrol,mhc_commonscreening,mhc_highriskvisitreason,mhc_maternalreport,mhc_pregnantscreenresult,mpi_babyinfo,mpi_patientinfo,mrm_diagnosis,mrm_fee,mrm_frontpage,mrm_operation,op_apply_info,op_record_info,opt_bloodtransfusionr,opt_deathrecords,pmc_premaritalrecord,psychosismedicine,psychosisrecord,psychosisvisit,ris_reg_info,ris_report_info,ybt_med_stock,ybt_outbound_order".split(
    ',')


def main():
    print(tables)
    print(tables.__len__())

    for table in tables:
        command_delete = '/data/software/confluent-3.3.0/bin/kafka-topics --delete --topic ' + table + ' --zookeeper 127.0.0.1:2181'
        try:
            print('正在执行: ' + table)
            os.system(command_delete)
            print('删除成功!')
        except Exception as e:
            print('执行失败', e)


if __name__ == '__main__':
    main()
