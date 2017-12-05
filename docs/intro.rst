概要
-------

本ガイドでは、AWS上でF5 WAF (BIG-IP LTM + ASM)の自動スケールのデプロイ方法
について説明します。IAMロールとELBの設定もこのガイドに含まれます。

AWS Marketplaceからテンプレートを起動します。 また、公式のF5 Networks GitHub
リポジトリから `AWS Launch Stack button <https://github.com/F5Networks/f5-aws-cloudformation/tree/master/supported/solutions/autoscale/waf#using-the-aws-launch-stack-button>`__ ボタンを使用することもできます。

**AWS の要件**
本ガイドを使用するには、次の前提条件を満たす必要があります。

.. NOTE::
   `Amazon EC2 でのセットアップ <http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html>`__
   
   `F5 Partner Resource Center (PRC)へのアクセスが可能な方は以下の資料をご参照ください <http://www.f5networks.co.jp/shared/pdf/AWS_easy_Setup_(multiAZ_and_AutoScaling)_20160921.pdf>`__

- AWSアカウント
- VPCでは `DNS hostnames <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/vpc-dns.html#vpc-dns-hostnames>`__ と `DNS resolution <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/vpc-dns.html#vpc-dns-hostnames>`__ がyesになっていること
- `Internet Gateway <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html>`__  ：インターネットアクセスに必要なInternetGatewayの設定
- 各availability zoneのF5 WAFとバックエンドサーバーの両方のSubnetsが設定されていること（ネットワーク図を参照）
- `Routes <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ 設定：サブネットの関連付けとインターネットゲートウェイが設定されていること
- `Security Groups <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ 設定：バックエンドサーバー用
  - ポート範囲=HTTP (TCP 80)、送信元=内部サブネット
- `Security Groups <http://docs.aws.amazon.com/ja_jp/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ 設定：F5 WAF インスタンス用:
  - ポート範囲=HTTP (TCP 80) 、送信元=内部サブネット、クライアント端末IP
  - ポート範囲=F5 WAF Management (TCP 8443) 、送信元=クライアント端末IP
  - ポート範囲=F5 WAF CLI (TCP 22) 、送信元=クライアント端末IP
- `EIP <http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-limit>`__：4個が利用可能になっていること 
- `EC2 Key pair <http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ ：F5 WAF VEへのSSHアクセス用
- バックエンドサーバー ｘ 2個(本ガイドではWordPressを使用)



**以下のAWS要件については、本ガイドで説明しています。**
  
- `IAM <http://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_roles.html>`__ ロール：必要となる権限の設定用
- `ELB <http://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/classic/elb-getting-started.html>`__ ： バックエンドサーバー用
- `ELB <http://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/classic/elb-getting-started.html>`__ ： F5 WAF VE用

.. NOTE::
  このCloudFormationテンプレート(以下、CFT)の公式の要件リストについては、以下を参照してください。
  
.. parsed-literal::
    
	 :raw_github_url:`/postman_collections/Class_1.postman_environment.json`