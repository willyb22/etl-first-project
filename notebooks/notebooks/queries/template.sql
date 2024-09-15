-- use this file on your code editor to write query and copy to the query on the notebooks
select
    case when c.holidaytype = '' then 'N' else 'Y' end as isholiday,
    ca.discount,
    ca.freeshppingflag,
    count(o.orderid) as count
from orders o
left join calendar c on o.orderdate=c.date
left join campaigns ca on o.campaignid=ca.campaignid
group by 
    isholiday,
    ca.discount,
    ca.freeshppingflag;