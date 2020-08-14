-- 테이블 순서는 관계를 고려하여 한 번에 실행해도 에러가 발생하지 않게 정렬되었습니다.

-- user Table Create SQL
CREATE TABLE user
(
    user_idx    INT             NOT NULL, 
    user_id     VARCHAR2(20)    NOT NULL, 
    password    VARCHAR2(20)    NOT NULL, 
    name        VARCHAR2(20)    NOT NULL, 
    birth       VARCHAR2(20)    NOT NULL, 
    tel         VARCHAR2(20)    NOT NULL, 
    grade       INT             DEFAULT 1 NOT NULL, 
    CONSTRAINT USER_PK PRIMARY KEY (user_idx)
)
/

CREATE SEQUENCE user_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER user_AI_TRG
BEFORE INSERT ON user 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT user_SEQ.NEXTVAL
    INTO :NEW.user_idx
    FROM DUAL;
END;
/

--DROP TRIGGER user_AI_TRG;
/

--DROP SEQUENCE user_SEQ;
/

COMMENT ON TABLE user IS '사용자'
/

COMMENT ON COLUMN user.user_idx IS '인덱스'
/

COMMENT ON COLUMN user.user_id IS '아이디'
/

COMMENT ON COLUMN user.password IS '패스워드'
/

COMMENT ON COLUMN user.name IS '이름'
/

COMMENT ON COLUMN user.birth IS '생일'
/

COMMENT ON COLUMN user.tel IS '전화번호'
/

COMMENT ON COLUMN user.grade IS '등급'
/

ALTER TABLE user
    ADD CONSTRAINT UC_user_id UNIQUE (user_id)
/


-- user Table Create SQL
CREATE TABLE restaurant
(
    r_idx          INT              NOT NULL, 
    name           VARCHAR2(20)     NULL, 
    category       VARCHAR2(20)     NULL, 
    price          INT              NULL, 
    image_url      VARCHAR2(200)    NULL, 
    distance       FLOAT            NULL, 
    score          FLOAT            NULL, 
    site_score     FLOAT            NULL, 
    review         INT              NULL, 
    site_review    INT              NULL, 
    main_menu      VARCHAR2(150)    NULL, 
    CONSTRAINT RESTAURANT_PK PRIMARY KEY (r_idx)
)
/

CREATE SEQUENCE restaurant_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER restaurant_AI_TRG
BEFORE INSERT ON restaurant 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT restaurant_SEQ.NEXTVAL
    INTO :NEW.r_idx
    FROM DUAL;
END;
/

--DROP TRIGGER restaurant_AI_TRG;
/

--DROP SEQUENCE restaurant_SEQ;
/

COMMENT ON TABLE restaurant IS '식당'
/

COMMENT ON COLUMN restaurant.r_idx IS '인덱스'
/

COMMENT ON COLUMN restaurant.name IS '식당명'
/

COMMENT ON COLUMN restaurant.category IS '카테고리'
/

COMMENT ON COLUMN restaurant.price IS '가격'
/

COMMENT ON COLUMN restaurant.image_url IS '이미지 주소'
/

COMMENT ON COLUMN restaurant.distance IS '거리'
/

COMMENT ON COLUMN restaurant.score IS '평점'
/

COMMENT ON COLUMN restaurant.site_score IS '사이트 점수'
/

COMMENT ON COLUMN restaurant.review IS '리뷰수'
/

COMMENT ON COLUMN restaurant.site_review IS '사이트 리뷰수'
/

COMMENT ON COLUMN restaurant.main_menu IS '대표메뉴'
/


-- user Table Create SQL
CREATE TABLE menu
(
    m_idx           INT              NOT NULL, 
    r_idx           INT              NULL, 
    menu            VARCHAR2(100)    NULL, 
    price           INT              NULL, 
    discount        INT              NULL, 
    discount_per    INT              NULL, 
    option          VARCHAR2(100)    NULL, 
    CONSTRAINT MENU_PK PRIMARY KEY (m_idx)
)
/

CREATE SEQUENCE menu_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER menu_AI_TRG
BEFORE INSERT ON menu 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT menu_SEQ.NEXTVAL
    INTO :NEW.m_idx
    FROM DUAL;
END;
/

--DROP TRIGGER menu_AI_TRG;
/

--DROP SEQUENCE menu_SEQ;
/

COMMENT ON TABLE menu IS '메뉴'
/

COMMENT ON COLUMN menu.m_idx IS '메뉴번호'
/

COMMENT ON COLUMN menu.r_idx IS '식당인덱스'
/

COMMENT ON COLUMN menu.menu IS '메뉴명'
/

COMMENT ON COLUMN menu.price IS '가격'
/

COMMENT ON COLUMN menu.discount IS '할인가'
/

COMMENT ON COLUMN menu.discount_per IS '할인율'
/

COMMENT ON COLUMN menu.option IS '옵션(1+1, 2+1)'
/

ALTER TABLE menu
    ADD CONSTRAINT FK_menu_r_idx_restaurant_r_idx FOREIGN KEY (r_idx)
        REFERENCES restaurant (r_idx)
/


-- user Table Create SQL
CREATE TABLE party
(
    p_idx          INT              NOT NULL, 
    title          VARCHAR2(150)    NULL, 
    user_id        VARCHAR2(20)     NULL, 
    cur_member     INT              NULL, 
    max_member     INT              NULL, 
    mamber_list    VARCHAR2         NULL, 
    status         INT              NULL, 
    CONSTRAINT PARTY_PK PRIMARY KEY (p_idx)
)
/

CREATE SEQUENCE party_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER party_AI_TRG
BEFORE INSERT ON party 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT party_SEQ.NEXTVAL
    INTO :NEW.p_idx
    FROM DUAL;
END;
/

--DROP TRIGGER party_AI_TRG;
/

--DROP SEQUENCE party_SEQ;
/

COMMENT ON TABLE party IS '파티모집'
/

COMMENT ON COLUMN party.p_idx IS '파티모집번호'
/

COMMENT ON COLUMN party.title IS '제목'
/

COMMENT ON COLUMN party.user_id IS '생성자'
/

COMMENT ON COLUMN party.cur_member IS '현재멤버'
/

COMMENT ON COLUMN party.max_member IS '최대멤버'
/

COMMENT ON COLUMN party.mamber_list IS '멤버리스트'
/

COMMENT ON COLUMN party.status IS '상태'
/

ALTER TABLE party
    ADD CONSTRAINT FK_party_user_id_user_user_id FOREIGN KEY (user_id)
        REFERENCES user (user_id)
/


-- user Table Create SQL
CREATE TABLE menu_reple
(
    mr_idx      INT             NOT NULL, 
    m_idx       INT             NULL, 
    user_id     VARCHAR2(20)    NULL, 
    comment     VARCHAR2(20)    NULL, 
    score       FLOAT           NULL, 
    rep_time    DATE            NULL, 
    status      INT             NULL, 
    CONSTRAINT MENU_REPLE_PK PRIMARY KEY (mr_idx)
)
/

CREATE SEQUENCE menu_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER menu_reple_AI_TRG
BEFORE INSERT ON menu_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT menu_reple_SEQ.NEXTVAL
    INTO :NEW.mr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER menu_reple_AI_TRG;
/

--DROP SEQUENCE menu_reple_SEQ;
/

COMMENT ON TABLE menu_reple IS '메뉴 댓글'
/

COMMENT ON COLUMN menu_reple.mr_idx IS '댓글번호'
/

COMMENT ON COLUMN menu_reple.m_idx IS '메뉴번호'
/

COMMENT ON COLUMN menu_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN menu_reple.comment IS '내용'
/

COMMENT ON COLUMN menu_reple.score IS '점수'
/

COMMENT ON COLUMN menu_reple.rep_time IS '시간'
/

COMMENT ON COLUMN menu_reple.status IS '상태'
/

ALTER TABLE menu_reple
    ADD CONSTRAINT FK_menu_reple_m_idx_menu_m_idx FOREIGN KEY (m_idx)
        REFERENCES menu (m_idx)
/

ALTER TABLE menu_reple
    ADD CONSTRAINT FK_menu_reple_user_id_user_use FOREIGN KEY (user_id)
        REFERENCES user (user_id)
/


-- user Table Create SQL
CREATE TABLE restaurant_reple
(
    rr_idx      INT             NOT NULL, 
    r_idx       INT             NULL, 
    user_id     VARCHAR2(20)    NULL, 
    comment     VARCHAR2(20)    NULL, 
    score       FLOAT           NULL, 
    rep_time    DATE            NULL, 
    status      INT             NULL, 
    CONSTRAINT RESTAURANT_REPLE_PK PRIMARY KEY (rr_idx)
)
/

CREATE SEQUENCE restaurant_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER restaurant_reple_AI_TRG
BEFORE INSERT ON restaurant_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT restaurant_reple_SEQ.NEXTVAL
    INTO :NEW.rr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER restaurant_reple_AI_TRG;
/

--DROP SEQUENCE restaurant_reple_SEQ;
/

COMMENT ON TABLE restaurant_reple IS '식당 댓글'
/

COMMENT ON COLUMN restaurant_reple.rr_idx IS '댓글번호'
/

COMMENT ON COLUMN restaurant_reple.r_idx IS '식당번호'
/

COMMENT ON COLUMN restaurant_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN restaurant_reple.comment IS '내용'
/

COMMENT ON COLUMN restaurant_reple.score IS '점수'
/

COMMENT ON COLUMN restaurant_reple.rep_time IS '시간'
/

COMMENT ON COLUMN restaurant_reple.status IS '상태'
/

ALTER TABLE restaurant_reple
    ADD CONSTRAINT FK_restaurant_reple_r_idx_rest FOREIGN KEY (r_idx)
        REFERENCES restaurant (r_idx)
/

ALTER TABLE restaurant_reple
    ADD CONSTRAINT FK_restaurant_reple_user_id_us FOREIGN KEY (user_id)
        REFERENCES user (user_id)
/


-- user Table Create SQL
CREATE TABLE party_reple
(
    pr_idx      INT              NOT NULL, 
    p_idx       INT              NULL, 
    user_id     VARCHAR2(20)     NULL, 
    comment     VARCHAR2(255)    NULL, 
    rep_time    DATE             NULL, 
    status      INT              NULL, 
    CONSTRAINT PARTY_REPLE_PK PRIMARY KEY (pr_idx)
)
/

CREATE SEQUENCE party_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER party_reple_AI_TRG
BEFORE INSERT ON party_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT party_reple_SEQ.NEXTVAL
    INTO :NEW.pr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER party_reple_AI_TRG;
/

--DROP SEQUENCE party_reple_SEQ;
/

COMMENT ON TABLE party_reple IS '파티댓글'
/

COMMENT ON COLUMN party_reple.pr_idx IS '팟댓글번호'
/

COMMENT ON COLUMN party_reple.p_idx IS '파티번호'
/

COMMENT ON COLUMN party_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN party_reple.comment IS '댓글'
/

COMMENT ON COLUMN party_reple.rep_time IS '단 시간'
/

COMMENT ON COLUMN party_reple.status IS '상태'
/

ALTER TABLE party_reple
    ADD CONSTRAINT FK_party_reple_p_idx_party_p_i FOREIGN KEY (p_idx)
        REFERENCES party (p_idx)
/

ALTER TABLE party_reple
    ADD CONSTRAINT FK_party_reple_user_id_user_us FOREIGN KEY (user_id)
        REFERENCES user (user_id)
/


