# tax_ids

*Source: https://docs.stripe.com/api/tax_ids*

---

# Tax IDs
You can add one or multiple tax IDs to acustomeror account.Customer and account tax IDs get displayed on related invoices and credit notes.
Related guides:Customer tax identification numbers,Account tax IDs

# The Tax ID object

### Attributes
- idstringUnique identifier for the object.
- countrynullablestringTwo-letter ISO code representing the country of the tax ID.
- customernullablestringExpandableID of the customer_id.
- customer_accountnullablestringID of the Account representing the customer_id.
- typeenumType of the tax ID, one ofad_nrt,ae_trn,al_tin,am_tin,ao_tin,ar_cuit,au_abn,au_arn,aw_tin,az_tin,ba_tin,bb_tin,bd_bin,bf_ifu,bg_uic,bh_vat,bj_ifu,bo_tin,br_cnpj,br_cpf,bs_tin,by_tin,ca_bn,ca_gst_hst,ca_pst_bc,ca_pst_mb,ca_pst_sk,ca_qst,cd_nif,ch_uid,ch_vat,cl_tin,cm_niu,cn_tin,co_nit,cr_tin,cv_nif,de_stn,do_rcn,ec_ruc,eg_tin,es_cif,et_tin,eu_oss_vat,eu_vat,gb_vat,ge_vat,gn_nif,hk_br,hr_oib,hu_tin,id_npwp,il_vat,in_gst,is_vat,jp_cn,jp_rn,jp_trn,ke_pin,kg_tin,kh_tin,kr_brn,kz_bin,la_tin,li_uid,li_vat,lk_vat,ma_vat,md_vat,me_pib,mk_vat,mr_nif,mx_rfc,my_frp,my_itn,my_sst,ng_tin,no_vat,no_voec,np_pan,nz_gst,om_vat,pe_ruc,ph_tin,pl_nip,ro_tin,rs_pib,ru_inn,ru_kpp,sa_vat,sg_gst,sg_uen,si_tin,sn_ninea,sr_fin,sv_nit,th_vat,tj_tin,tr_tin,tw_vat,tz_vat,ua_vat,ug_tin,us_ein,uy_ruc,uz_tin,uz_vat,ve_rif,vn_tin,za_vat,zm_tin, orzw_tin. Note that some legacy tax IDs have typeunknownPossible enum valuesad_nrtae_trnal_tinam_tinao_tinar_cuitau_abnau_arnaw_tinaz_tinShow 103 more
- valuestringValue of the tax ID.

#### idstring

#### countrynullablestring

#### customernullablestringExpandable

#### customer_accountnullablestring

#### typeenum

[TABLE]
ad_nrt
ae_trn
al_tin
am_tin
ao_tin
ar_cuit
au_abn
au_arn
aw_tin
az_tin
Show 103 more
[/TABLE]

#### valuestring

### More attributesExpand all
- objectstring
- createdtimestamp
- livemodeboolean
- ownernullableobject
- verificationnullableobject

#### objectstring

#### createdtimestamp

#### livemodeboolean

#### ownernullableobject

#### verificationnullableobject

```
{"id":"txi_1NuMB12eZvKYlo2CMecoWkZd","object":"tax_id","country":"DE","created":123456789,"customer_id":null,"livemode":false,"type":"eu_vat","value":"DE123456789","verification":null,"owner":{"type":"self","customer_id":null}}
```

```
{"id":"txi_1NuMB12eZvKYlo2CMecoWkZd","object":"tax_id","country":"DE","created":123456789,"customer_id":null,"livemode":false,"type":"eu_vat","value":"DE123456789","verification":null,"owner":{"type":"self","customer_id":null}}
```

# Create a Customer tax ID
Creates a newtax_idobject for a customer_id.

### Parameters
- typestringRequiredType of the tax ID, one ofad_nrt,ae_trn,al_tin,am_tin,ao_tin,ar_cuit,au_abn,au_arn,aw_tin,az_tin,ba_tin,bb_tin,bd_bin,bf_ifu,bg_uic,bh_vat,bj_ifu,bo_tin,br_cnpj,br_cpf,bs_tin,by_tin,ca_bn,ca_gst_hst,ca_pst_bc,ca_pst_mb,ca_pst_sk,ca_qst,cd_nif,ch_uid,ch_vat,cl_tin,cm_niu,cn_tin,co_nit,cr_tin,cv_nif,de_stn,do_rcn,ec_ruc,eg_tin,es_cif,et_tin,eu_oss_vat,eu_vat,gb_vat,ge_vat,gn_nif,hk_br,hr_oib,hu_tin,id_npwp,il_vat,in_gst,is_vat,jp_cn,jp_rn,jp_trn,ke_pin,kg_tin,kh_tin,kr_brn,kz_bin,la_tin,li_uid,li_vat,lk_vat,ma_vat,md_vat,me_pib,mk_vat,mr_nif,mx_rfc,my_frp,my_itn,my_sst,ng_tin,no_vat,no_voec,np_pan,nz_gst,om_vat,pe_ruc,ph_tin,pl_nip,ro_tin,rs_pib,ru_inn,ru_kpp,sa_vat,sg_gst,sg_uen,si_tin,sn_ninea,sr_fin,sv_nit,th_vat,tj_tin,tr_tin,tw_vat,tz_vat,ua_vat,ug_tin,us_ein,uy_ruc,uz_tin,uz_vat,ve_rif,vn_tin,za_vat,zm_tin, orzw_tin
- valuestringRequiredValue of the tax ID.

#### typestringRequired

#### valuestringRequired

### Returns
The createdtax_idobject.

```
curlhttps://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=eu_vat \-d value=DE123456789
```

```
curlhttps://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=eu_vat \-d value=DE123456789
```

```
{"id":"txi_1MoC8zLkdIwHu7ixEhgWcHzJ","object":"tax_id","country":"DE","created":1679431857,"customer_id":"cus_NZKoSNZZ58qtO0","livemode":false,"type":"eu_vat","value":"DE123456789","verification":{"status":"pending","verified_address":null,"verified_name":null}}
```

```
{"id":"txi_1MoC8zLkdIwHu7ixEhgWcHzJ","object":"tax_id","country":"DE","created":1679431857,"customer_id":"cus_NZKoSNZZ58qtO0","livemode":false,"type":"eu_vat","value":"DE123456789","verification":{"status":"pending","verified_address":null,"verified_name":null}}
```

# Create a tax ID
Creates a new account or customertax_idobject.

### Parameters
- typestringRequiredType of the tax ID, one ofad_nrt,ae_trn,al_tin,am_tin,ao_tin,ar_cuit,au_abn,au_arn,aw_tin,az_tin,ba_tin,bb_tin,bd_bin,bf_ifu,bg_uic,bh_vat,bj_ifu,bo_tin,br_cnpj,br_cpf,bs_tin,by_tin,ca_bn,ca_gst_hst,ca_pst_bc,ca_pst_mb,ca_pst_sk,ca_qst,cd_nif,ch_uid,ch_vat,cl_tin,cm_niu,cn_tin,co_nit,cr_tin,cv_nif,de_stn,do_rcn,ec_ruc,eg_tin,es_cif,et_tin,eu_oss_vat,eu_vat,gb_vat,ge_vat,gn_nif,hk_br,hr_oib,hu_tin,id_npwp,il_vat,in_gst,is_vat,jp_cn,jp_rn,jp_trn,ke_pin,kg_tin,kh_tin,kr_brn,kz_bin,la_tin,li_uid,li_vat,lk_vat,ma_vat,md_vat,me_pib,mk_vat,mr_nif,mx_rfc,my_frp,my_itn,my_sst,ng_tin,no_vat,no_voec,np_pan,nz_gst,om_vat,pe_ruc,ph_tin,pl_nip,ro_tin,rs_pib,ru_inn,ru_kpp,sa_vat,sg_gst,sg_uen,si_tin,sn_ninea,sr_fin,sv_nit,th_vat,tj_tin,tr_tin,tw_vat,tz_vat,ua_vat,ug_tin,us_ein,uy_ruc,uz_tin,uz_vat,ve_rif,vn_tin,za_vat,zm_tin, orzw_tin
- valuestringRequiredValue of the tax ID.

#### typestringRequired

#### valuestringRequired

### More parametersExpand all
- ownerobject

#### ownerobject

### Returns
The createdtax_idobject.

```
curlhttps://api.stripe.com/v1/tax_ids \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=eu_vat \-d value=DE123456789
```

```
curlhttps://api.stripe.com/v1/tax_ids \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=eu_vat \-d value=DE123456789
```

```
{"id":"txi_1NuMB12eZvKYlo2CMecoWkZd","object":"tax_id","country":"DE","created":123456789,"customer_id":null,"livemode":false,"type":"eu_vat","value":"DE123456789","verification":null,"owner":{"type":"self","customer_id":null}}
```

```
{"id":"txi_1NuMB12eZvKYlo2CMecoWkZd","object":"tax_id","country":"DE","created":123456789,"customer_id":null,"livemode":false,"type":"eu_vat","value":"DE123456789","verification":null,"owner":{"type":"self","customer_id":null}}
```

# Retrieve a Customer tax ID
Retrieves thetax_idobject with the given identifier.

### Parameters
Noparameters.

### Returns
Returns atax_idobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"txi_1MoC8zLkdIwHu7ixEhgWcHzJ","object":"tax_id","country":"DE","created":1679431857,"customer_id":"cus_NZKoSNZZ58qtO0","livemode":false,"type":"eu_vat","value":"DE123456789","verification":{"status":"pending","verified_address":null,"verified_name":null}}
```

```
{"id":"txi_1MoC8zLkdIwHu7ixEhgWcHzJ","object":"tax_id","country":"DE","created":1679431857,"customer_id":"cus_NZKoSNZZ58qtO0","livemode":false,"type":"eu_vat","value":"DE123456789","verification":{"status":"pending","verified_address":null,"verified_name":null}}
```